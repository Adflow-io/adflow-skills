#!/usr/bin/env python3
"""
Instagram comment-reply bubbel — herbruikbaar component (zusje van tiktok_comment.py).

Witte afgeronde kaart met avatar, commenttekst (emoji mag) en daaronder grijs "Replying to <user>".
Breedte krimpt mee met de tekst tot een maximum; langere tekst loopt naar beneden door.
Maten zijn pixel-gemeten op drie voorbeelden (kort / normaal / lang).

Gebruik als module:
    from instagram_comment import render_instagram_comment
    render_instagram_comment("test", "Create your custom Instagram comment 🔥").save("ig.png")

Gebruik als CLI:
    python3 scripts/instagram_comment.py -u test -c "Create your custom Instagram comment 🔥" -o ig.png
    python3 scripts/instagram_comment.py -u test -c "..." --video in.mp4 -o out.mp4 --start 0 --end 3
    python3 scripts/instagram_comment.py -u test -c "..." -o ig.png --invert
    python3 scripts/instagram_comment.py --batch comments.json   # lijst van {"username","comment","out",...}

Lettertype: Inter (scripts/fonts/Inter.ttf, OFL), tekst-optiek (opsz 14), Regular.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tiktok_comment import (  # noqa: E402  gedeelde helpers
    EMOJI_FONT, EMOJI_NATIVE, POSITIONS, SS, blur_name, _runs, _truncate, _video_width, _wrap_words, overlay_on_video,
)

FONT_DIR = Path(__file__).resolve().parent / "fonts"
INTER = FONT_DIR / "Inter.ttf"

# 1.0 = juiste maat voor een 1080 px brede video. Het voorbeeld is gemeten op 1x; ×1.75 geeft
# dezelfde visuele grootte als de TikTok-bubbel (max. ~850 px breed op 1080).
VIDEO_SCALE = 1.75

THEMES = {
    "light": {"bg": (255, 255, 255, 255), "text": (0, 0, 0, 255), "sub": (125, 125, 125, 255),
              "avatar_bg": (244, 245, 247, 255), "avatar_fg": (132, 136, 147, 255)},
    "invert": {"bg": (0, 0, 0, 255), "text": (255, 255, 255, 255), "sub": (150, 150, 150, 255),
               "avatar_bg": (48, 49, 52, 255), "avatar_fg": (130, 134, 144, 255)},
}

# Alle maten in pixels van het voorbeeld (1x), baseline = onderkant van de letters.
BASE = {
    "max_width": 486,      # maximale kaartbreedte
    "text_x": 108,         # linkerrand kaart -> tekst
    "pad_right": 31,       # tekst (advance) -> rechterrand bij meekrimpen
    "avatar": 56,
    "avatar_x": 30,
    "avatar_y": 30,
    "text_size": 30.3,     # Inter Regular, kapitaalhoogte 22
    "sub_size": 23.9,      # "Replying to", kapitaalhoogte 18
    "first_baseline": 58,  # bovenkant -> baseline eerste regel
    "line": 36,            # regelafstand comment
    "sub_gap": 52,         # baseline laatste regel -> baseline "Replying to"
    "bottom": 36,          # baseline "Replying to" -> onderkant
    "radius": 31,
}
# schaduw (teruggerekend uit het voorbeeld): twee lagen (blur, y-offset, dekking)
SHADOWS = [(2, 4, 0.06), (10, 20, 0.08)]


def _inter(size: float, weight: int = 400) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(INTER), size)
    f.set_variation_by_axes([14, weight])  # opsz 14 = tekst-optiek (breder), zoals in het voorbeeld
    return f


class _IGType:
    """Tekst + Apple-emoji op dezelfde baseline; emoji op em-maat (niet bijgesneden)."""

    def __init__(self, font: ImageFont.FreeTypeFont, size: float):
        self.font, self.size = font, size
        self.em = size * 0.95        # emoji-hoogte (voorbeeld: 28 px bij tekst 30.3)
        self.drop = size * 0.16      # emoji zakt iets onder de baseline
        self.lead = size * 0.06      # extra ruimte vóór een emoji
        try:
            self.efont = ImageFont.truetype(EMOJI_FONT, EMOJI_NATIVE)
        except OSError:
            self.efont = None

    def width(self, s: str) -> float:
        return sum((self.lead + self.em) if (e and self.efont) else self.font.getlength(p) for e, p in _runs(s))

    def draw(self, canvas: Image.Image, x: float, baseline: float, s: str, fill) -> None:
        d = ImageDraw.Draw(canvas)
        for e, part in _runs(s):
            if e and self.efont:
                n = EMOJI_NATIVE
                im = Image.new("RGBA", (int(n * 1.3), n), (0, 0, 0, 0))
                ImageDraw.Draw(im).text((0, n), part, font=self.efont, embedded_color=True, anchor="ls")
                im = im.crop((0, 0, n, n)).resize((max(1, int(self.em)), max(1, int(self.em))), Image.LANCZOS)
                canvas.alpha_composite(im, (int(x + self.lead), int(baseline + self.drop - self.em)))
                x += self.lead + self.em
            else:
                d.text((x, baseline), part, font=self.font, fill=fill, anchor="ls")
                x += self.font.getlength(part)


def _avatar(source, size: int, colors: dict) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    if source and Path(source).exists():
        img = ImageOps.fit(Image.open(source).convert("RGBA"), (size, size), Image.LANCZOS)
    else:
        img = Image.new("RGBA", (size, size), colors["avatar_bg"])
        d = ImageDraw.Draw(img)
        u = size / 56  # gemeten op een avatar van 56 px
        d.ellipse(((27.5 - 10.75) * u, (22.5 - 10.75) * u, (27.5 + 10.75) * u, (22.5 + 10.75) * u), fill=colors["avatar_fg"])
        d.ellipse(((27.5 - 23.5) * u, 38 * u, (27.5 + 23.5) * u, 85 * u), fill=colors["avatar_fg"])
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def _card(bw: int, bh: int, radius: int, k: float, fill, shadow: bool) -> tuple[Image.Image, int]:
    """Kaart met schaduw; geeft (canvas, marge) terug."""
    margin = int(60 * k) if shadow else SS
    W, H = bw + 2 * margin, bh + 2 * margin
    shape = Image.new("L", (W, H), 0)
    ImageDraw.Draw(shape).rounded_rectangle((margin, margin, margin + bw - 1, margin + bh - 1), radius=radius, fill=255)
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if shadow:
        for blur, oy, alpha in SHADOWS:
            layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            layer.putalpha(shape.point(lambda p, a=alpha: int(p * a)))
            layer = layer.filter(ImageFilter.GaussianBlur(blur * k))
            shifted = Image.new("RGBA", (W, H), (0, 0, 0, 0))
            shifted.paste(layer, (0, int(oy * k)))
            canvas = Image.alpha_composite(canvas, shifted)
    canvas.paste(Image.new("RGBA", (W, H), fill), (0, 0), shape)
    return canvas, margin


def render_instagram_comment(
    username: str,
    comment: str,
    avatar: str | Path | None = None,
    *,
    scale: float = 1.0,
    theme: str = "light",
    width: int | None = None,
    fit: bool = True,
    max_lines: int | None = None,
    sub: str | None = None,
    shadow: bool = True,
    blur: bool | str = False,
) -> Image.Image:
    """
    Geeft een RGBA-afbeelding van de Instagram comment-reply kaart terug.

    scale   1.0 = juiste maat voor 1080 px brede video
    theme   "light" (standaard, wit) of "invert" (zwart met witte tekst)
    width   maximale kaartbreedte in voorbeeld-pixels (standaard 486)
    fit     True (standaard, zoals Instagram) = kaart krimpt mee bij korte tekst; False = altijd max. breed
    sub     eigen onderregel i.p.v. "Replying to {user}"
    """
    if theme == "dark":
        theme = "invert"
    colors = THEMES[theme]
    k = scale * VIDEO_SCALE * SS
    s = {key: v * k for key, v in BASE.items()}
    if width:
        s["max_width"] = width * k

    ft, fs = _inter(s["text_size"]), _inter(s["sub_size"])
    tt, ts = _IGType(ft, s["text_size"]), _IGType(fs, s["sub_size"])
    name = username.strip().lstrip("@")
    sub_text = (sub or "Replying to {user}").format(user=name)

    text_max = s["max_width"] - s["text_x"] - s["pad_right"]
    lines = _truncate(_wrap_words(comment.strip(), tt, text_max), tt, text_max, max_lines)
    sub_lines = _wrap_words(sub_text, ts, text_max)

    content = max([tt.width(l) for l in lines] + [ts.width(l) for l in sub_lines])
    # zoals in het voorbeeld: zodra de tekst moet afbreken staat de kaart op maximale breedte,
    # past alles op één regel dan krimpt hij mee
    bw = int(s["max_width"])
    wrapped = len(lines) > len(comment.strip().split("\n"))
    if fit and not wrapped:
        bw = int(min(bw, s["text_x"] + content + s["pad_right"]))
    last = s["first_baseline"] + (len(lines) - 1) * s["line"]
    sub_last = last + s["sub_gap"] + (len(sub_lines) - 1) * s["line"] * 0.8
    bh = int(max(sub_last + s["bottom"], s["avatar_y"] * 2 + s["avatar"]))

    canvas, m = _card(bw, bh, int(s["radius"]), k, colors["bg"], shadow)
    canvas.alpha_composite(_avatar(avatar, int(s["avatar"]), colors), (int(m + s["avatar_x"]), int(m + s["avatar_y"])))
    for n, line in enumerate(lines):
        tt.draw(canvas, m + s["text_x"], m + s["first_baseline"] + n * s["line"], line, colors["text"])
    for n, line in enumerate(sub_lines):
        ts.draw(canvas, m + s["text_x"], m + last + s["sub_gap"] + n * s["line"] * 0.8, line, colors["sub"])
        if blur:
            blur_name(canvas, ts, m + s["text_x"], m + last + s["sub_gap"] + n * s["line"] * 0.8, line, name, blur)
    # BOX: geen overshoot, zodat de grijswaarden exact blijven
    return canvas.resize((max(1, canvas.width // SS), max(1, canvas.height // SS)), Image.BOX)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Instagram comment-reply kaart renderen (PNG of over video).")
    p.add_argument("-u", "--username")
    p.add_argument("-c", "--comment")
    p.add_argument("-a", "--avatar")
    p.add_argument("-o", "--out")
    p.add_argument("--invert", action="store_true", help="zwarte kaart met witte tekst")
    p.add_argument("--scale", type=float, help="standaard: videobreedte/1080, of 1.0 zonder video")
    p.add_argument("--width", type=int, help="maximale breedte in voorbeeld-pixels (standaard 486)")
    p.add_argument("--fixed", action="store_true", help="altijd maximale breedte, niet meekrimpen")
    p.add_argument("--max-lines", type=int)
    p.add_argument("--sub", help='eigen onderregel, bv. "Antwoord aan {user}"')
    p.add_argument("--no-shadow", action="store_true")
    p.add_argument("--blur-name", nargs="?", const="all", choices=["all", "last"],
                   help="naam vervagen: zonder waarde de hele naam, 'last' = alleen de achternaam")
    p.add_argument("--video")
    p.add_argument("--start", type=float)
    p.add_argument("--end", type=float)
    p.add_argument("--position", choices=list(POSITIONS), default="top")
    p.add_argument("--batch")
    args = p.parse_args(argv)

    if args.batch:
        jobs = json.loads(Path(args.batch).read_text())
    else:
        if not (args.username and args.comment and args.out):
            p.error("--username, --comment en --out zijn verplicht (of gebruik --batch)")
        jobs = [{"username": args.username, "comment": args.comment, "avatar": args.avatar, "out": args.out,
                 "video": args.video, "start": args.start, "end": args.end}]
    for job in jobs:
        video = Path(job["video"]) if job.get("video") else None
        scale = job.get("scale") or args.scale or (_video_width(video) / 1080 if video else 1.0)
        img = render_instagram_comment(
            job["username"], job["comment"], job.get("avatar"), scale=scale,
            theme=job.get("theme", "invert" if args.invert else "light"), width=job.get("width", args.width),
            fit=not job.get("fixed", args.fixed), max_lines=job.get("max_lines", args.max_lines),
            sub=job.get("sub", args.sub), shadow=not args.no_shadow, blur=job.get("blur_name", args.blur_name),
        )
        out = Path(job["out"])
        if video:
            png = out.with_suffix(".comment.png")
            img.save(png)
            overlay_on_video(png, video, out, job.get("start"), job.get("end"), job.get("position", args.position))
            print(f"✓ {out}  (kaart: {png})")
        else:
            img.save(out)
            print(f"✓ {out}  ({img.width}×{img.height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
