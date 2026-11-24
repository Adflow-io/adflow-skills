#!/usr/bin/env python3
"""
Facebook comment — herbruikbaar component.

Profielfoto links, grijze afgeronde bubbel met naam (vet) en commenttekst, daaronder
"45m   Like   Reply" en standaard rechts een like-teller met blauw duimpje.
Bubbel krimpt mee bij korte tekst; zodra de tekst afbreekt staat hij op maximale breedte
en loopt de tekst naar beneden door.

Gebruik als module:
    from facebook_comment import render_facebook_comment
    render_facebook_comment("Paulo Givenchy", "Who would buy this defenders??", likes=1).save("fb.png")

Gebruik als CLI:
    python3 scripts/facebook_comment.py -n "Paulo Givenchy" -c "Who would buy this defenders??" -o fb.png
    python3 scripts/facebook_comment.py -n "John Page" -c "..." --time 45m --no-like -o fb.png
    python3 scripts/facebook_comment.py -n "..." -c "..." --avatar foto.jpg --likes 12 -o fb.png
    python3 scripts/facebook_comment.py -n "..." -c "..." --video in.mp4 -o out.mp4 --start 0 --end 3
    python3 scripts/facebook_comment.py --batch comments.json   # lijst van {"name","comment","out",...}

Maten afgelezen van een Android-screenshot op 1080 px breed (schaal 1.0 = 1080 px video).
Lettertype: Roboto (scripts/fonts/Roboto.ttf, OFL; Android-look zoals het voorbeeld), anders SF Pro.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

sys.path.insert(0, str(Path(__file__).resolve().parent))
from instagram_comment import _IGType  # noqa: E402
from tiktok_comment import POSITIONS, SS, _truncate, _video_width, _wrap_words, overlay_on_video  # noqa: E402

FONT_DIR = Path(__file__).resolve().parent / "fonts"
ROBOTO = FONT_DIR / "Roboto.ttf"
SF_PRO = Path("/System/Library/Fonts/SFNS.ttf")

THEMES = {
    "light": {"bubble": (240, 242, 245, 255), "name": (5, 5, 5, 255), "text": (5, 5, 5, 255),
              "meta": (101, 103, 107, 255), "avatar_bg": (201, 204, 209, 255), "avatar_fg": (255, 255, 255, 255),
              "ring": (255, 255, 255, 255), "page": (255, 255, 255, 255)},
    "invert": {"bubble": (58, 59, 60, 255), "name": (228, 230, 235, 255), "text": (228, 230, 235, 255),
               "meta": (176, 179, 184, 255), "avatar_bg": (78, 79, 80, 255), "avatar_fg": (176, 179, 184, 255),
               "ring": (36, 37, 38, 255), "page": (36, 37, 38, 255)},
}
LIKE_BLUE_TOP, LIKE_BLUE_BOTTOM = (24, 160, 251), (8, 102, 255)

# maten in pixels van het voorbeeld (1080 breed), baseline = onderkant van de letters
BASE = {
    "avatar": 118, "avatar_x": 25, "avatar_y": 28,
    "bubble_x": 178, "bubble_y": 28, "max_width": 823, "radius": 54,
    "text_x": 43,          # bubbelrand -> tekst
    "pad_right": 52,       # tekst -> rechterrand bij meekrimpen
    # lettergroottes staan per font in FONT_SPECS (gemeten op de regelbreedtes van het voorbeeld)
    "name_baseline": 65,   # bovenkant bubbel -> baseline naam
    "text_gap": 66,        # baseline naam -> baseline eerste regel
    "line": 62.5,          # regelafstand comment
    "bottom": 37,          # baseline laatste regel -> onderkant bubbel
    "meta_gap": 73,        # onderkant bubbel -> baseline "45m Like Reply"
    "meta_space": 70,      # ruimte tussen "45m", "Like", "Reply"
    "like_d": 52,          # duimpje (diameter)
    "like_right": 37,      # duimpje steekt zoveel voorbij de rechterrand van de bubbel uit
    "like_num_gap": 19,    # teller -> duimpje
    "pad_bottom": 30,
}


# (bestand, {rol: (grootte, gewicht)})  — Roboto = Android (zoals het voorbeeld), SF Pro = iPhone
FONT_SPECS = {
    "roboto": (ROBOTO, {"name": (42.0, "Bold"), "text": (47.7, "Regular"),
                        "meta": (42.7, "Regular"), "meta_bold": (42.7, "Bold")}),
    "sf":     (SF_PRO, {"name": (43.0, "Semibold"), "text": (50.5, "Regular"),
                        "meta": (43.0, "Regular"), "meta_bold": (43.0, "Semibold")}),
}


def _role_font(role: str, k: float) -> tuple[ImageFont.FreeTypeFont, float]:
    path, roles = FONT_SPECS["roboto" if ROBOTO.exists() else "sf"]
    size, weight = roles[role]
    f = ImageFont.truetype(str(path), size * k)
    f.set_variation_by_name(weight)
    return f, size * k


def _font(size: float, weight: str) -> ImageFont.FreeTypeFont:
    if ROBOTO.exists():
        f = ImageFont.truetype(str(ROBOTO), size)
        try:
            f.set_variation_by_name(weight)
        except Exception:
            pass
        return f
    f = ImageFont.truetype(str(SF_PRO), size)
    f.set_variation_by_name(weight)
    return f


def _avatar(source, size: int, colors: dict, k: float) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    if source and Path(source).exists():
        img = ImageOps.fit(Image.open(source).convert("RGBA"), (size, size), Image.LANCZOS)
    else:
        img = Image.new("RGBA", (size, size), colors["avatar_bg"])
        d = ImageDraw.Draw(img)
        u = size / 100
        d.ellipse((34 * u, 20 * u, 66 * u, 54 * u), fill=colors["avatar_fg"])
        d.ellipse((16 * u, 60 * u, 84 * u, 128 * u), fill=colors["avatar_fg"])
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    # dun lichtgrijs randje zoals in de app
    ImageDraw.Draw(out).ellipse((0, 0, size - 1, size - 1), outline=(0, 0, 0, 22), width=max(1, int(1.5 * k)))
    return out


def _like_icon(d: int, ring: tuple) -> Image.Image:
    """Blauw rondje met witte duim (Facebook-like), met witte rand."""
    im = Image.new("RGBA", (d, d), (0, 0, 0, 0))
    grad = Image.new("RGBA", (1, d))
    for y in range(d):
        t = y / max(1, d - 1)
        grad.putpixel((0, y), tuple(round(a + (b - a) * t) for a, b in zip(LIKE_BLUE_TOP, LIKE_BLUE_BOTTOM)) + (255,))
    grad = grad.resize((d, d))
    mask = Image.new("L", (d, d), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, d - 1, d - 1), fill=255)
    ImageDraw.Draw(im).ellipse((0, 0, d - 1, d - 1), fill=ring)
    inner = Image.new("L", (d, d), 0)
    rw = d * 0.06
    ImageDraw.Draw(inner).ellipse((rw, rw, d - 1 - rw, d - 1 - rw), fill=255)
    im.paste(grad, (0, 0), inner)
    dr = ImageDraw.Draw(im)
    u = d / 100
    w = (255, 255, 255, 255)
    dr.rounded_rectangle((27 * u, 47 * u, 36 * u, 74 * u), radius=2 * u, fill=w)            # manchet
    dr.rounded_rectangle((40 * u, 44 * u, 73 * u, 74 * u), radius=6 * u, fill=w)            # hand
    dr.polygon([(41 * u, 46 * u), (50 * u, 27 * u), (55 * u, 25 * u), (58 * u, 30 * u),
                (56 * u, 44 * u), (41 * u, 48 * u)], fill=w)                                    # duim
    return im


def render_facebook_comment(
    name: str,
    comment: str,
    avatar: str | Path | None = None,
    *,
    time: str = "1m",
    likes: int | None = 1,
    scale: float = 1.0,
    theme: str = "light",
    width: int | None = None,
    fit: bool = True,
    max_lines: int | None = None,
    background: bool = False,
    like_label: str = "Like",
    reply_label: str = "Reply",
) -> Image.Image:
    """
    likes       aantal likes rechtsonder met blauw duimpje (standaard 1); None of 0 = geen like
    time        tijd links onder de bubbel ("45m", "9h", "2d")
    background  True = witte (of donkere) pagina-achtergrond i.p.v. transparant
    """
    if theme == "dark":
        theme = "invert"
    c = THEMES[theme]
    k = scale * SS
    s = {key: v * k for key, v in BASE.items()}
    if width:
        s["max_width"] = width * k

    tn = _IGType(*_role_font("name", k))
    tt = _IGType(*_role_font("text", k))
    fm_reg, fm_bold = _role_font("meta", k)[0], _role_font("meta_bold", k)[0]

    text_max = s["max_width"] - s["text_x"]  # afgeleid: "Given United's current predicament" past nog op één regel
    lines = _truncate(_wrap_words(comment.strip(), tt, text_max), tt, text_max, max_lines)
    wrapped = len(lines) > len(comment.strip().split("\n"))
    content = max([tn.width(name)] + [tt.width(l) for l in lines])
    bw = s["max_width"] if wrapped or not fit else min(s["max_width"], s["text_x"] + content + s["pad_right"])
    last = s["name_baseline"] + s["text_gap"] + (len(lines) - 1) * s["line"]
    bh = last + s["bottom"]

    bx, by = s["bubble_x"], s["bubble_y"]
    meta_base = by + bh + s["meta_gap"]
    show_like = bool(likes)
    right = bx + bw + (s["like_right"] if show_like else 0) + 20 * k
    W, H = int(right), int(meta_base + s["pad_bottom"])
    canvas = Image.new("RGBA", (W, H), c["page"] if background else (0, 0, 0, 0))
    d = ImageDraw.Draw(canvas)

    canvas.alpha_composite(_avatar(avatar, int(s["avatar"]), c, k), (int(s["avatar_x"]), int(s["avatar_y"])))
    d.rounded_rectangle((bx, by, bx + bw, by + bh), radius=s["radius"], fill=c["bubble"])
    tn.draw(canvas, bx + s["text_x"], by + s["name_baseline"], name, c["name"])
    for n, line in enumerate(lines):
        tt.draw(canvas, bx + s["text_x"], by + s["name_baseline"] + s["text_gap"] + n * s["line"], line, c["text"])

    x = bx + s["text_x"]
    for label, f in ((time, fm_reg), (like_label, fm_bold), (reply_label, fm_bold)):
        d.text((x, meta_base), label, font=f, fill=c["meta"], anchor="ls")
        x += f.getlength(label) + s["meta_space"]

    if show_like:
        ld = int(s["like_d"])
        icon_x = int(bx + bw + s["like_right"] - ld)
        cap = fm_reg.getbbox("1", anchor="ls")[1]  # negatief: hoogte boven baseline
        icon_y = int(meta_base + cap / 2 - ld / 2)
        canvas.alpha_composite(_like_icon(ld, c["ring"] if background else (255, 255, 255, 255)), (icon_x, icon_y))
        num = str(likes)
        d.text((icon_x - s["like_num_gap"] - fm_reg.getlength(num), meta_base), num, font=fm_reg, fill=c["meta"], anchor="ls")

    return canvas.resize((max(1, W // SS), max(1, H // SS)), Image.BOX)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Facebook comment renderen (PNG of over video).")
    p.add_argument("-n", "--name")
    p.add_argument("-c", "--comment")
    p.add_argument("-a", "--avatar")
    p.add_argument("-o", "--out")
    p.add_argument("--time", default="1m", help='tijd onder de bubbel, bv. "45m", "9h"')
    p.add_argument("--likes", type=int, default=1, help="aantal likes (standaard 1)")
    p.add_argument("--no-like", action="store_true", help="zonder like-teller en duimpje")
    p.add_argument("--invert", action="store_true", help="donkere modus")
    p.add_argument("--background", action="store_true", help="pagina-achtergrond i.p.v. transparant")
    p.add_argument("--scale", type=float, help="standaard: videobreedte/1080, of 1.0 zonder video")
    p.add_argument("--width", type=int, help="maximale bubbelbreedte (standaard 823)")
    p.add_argument("--fixed", action="store_true", help="altijd maximale breedte")
    p.add_argument("--max-lines", type=int)
    p.add_argument("--video")
    p.add_argument("--start", type=float)
    p.add_argument("--end", type=float)
    p.add_argument("--position", choices=list(POSITIONS), default="top")
    p.add_argument("--batch")
    args = p.parse_args(argv)

    if args.batch:
        jobs = json.loads(Path(args.batch).read_text())
    else:
        if not (args.name and args.comment and args.out):
            p.error("--name, --comment en --out zijn verplicht (of gebruik --batch)")
        jobs = [{"name": args.name, "comment": args.comment, "avatar": args.avatar, "out": args.out,
                 "video": args.video, "start": args.start, "end": args.end}]
    for job in jobs:
        video = Path(job["video"]) if job.get("video") else None
        scale = job.get("scale") or args.scale or (_video_width(video) / 1080 if video else 1.0)
        likes = None if (job.get("no_like", args.no_like)) else job.get("likes", args.likes)
        img = render_facebook_comment(
            job["name"], job["comment"], job.get("avatar"), time=job.get("time", args.time), likes=likes,
            scale=scale, theme=job.get("theme", "invert" if args.invert else "light"),
            width=job.get("width", args.width), fit=not job.get("fixed", args.fixed),
            max_lines=job.get("max_lines", args.max_lines), background=job.get("background", args.background),
        )
        out = Path(job["out"])
        if video:
            png = out.with_suffix(".comment.png")
            img.save(png)
            overlay_on_video(png, video, out, job.get("start"), job.get("end"), job.get("position", args.position))
            print(f"✓ {out}  (comment: {png})")
        else:
            img.save(out)
            print(f"✓ {out}  ({img.width}×{img.height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
