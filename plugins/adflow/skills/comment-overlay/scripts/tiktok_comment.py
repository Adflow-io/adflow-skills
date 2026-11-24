#!/usr/bin/env python3
"""
TikTok "Reply to <user>'s comment" bubbel — herbruikbaar component.

Rendert de witte comment-reply sticker (avatar + "Reply to X's comment" + commenttekst, met emoji)
als transparante PNG, en kan hem optioneel direct over een video leggen met ffmpeg.

Gebruik als module:
    from tiktok_comment import render_comment_reply
    render_comment_reply("username", "Write any comment and see what happens 😊").save("c.png")

Gebruik als CLI:
    python3 scripts/tiktok_comment.py -u "username" -c "Werkt dit ook bij krullend haar? 😊" -o comment.png
    python3 scripts/tiktok_comment.py -u "username" -c "..." --video in.mp4 -o out.mp4 --start 0 --end 3
    python3 scripts/tiktok_comment.py --batch comments.json   # lijst van {"username","comment","out",...}

Gedrag (zoals het TikTok-voorbeeld):
- Avatar staat vast linksboven; zonder --avatar komt er het grijze standaard-profielicoon.
- Kopregel breekt op in blokken: "Reply to" / gebruikersnaam / "'s comment" als het niet op één regel past.
- Vaste bubbelbreedte; commenttekst loopt naar beneden door over zoveel regels als nodig (optioneel afkappen met --max-lines, meekrimpen met --fit).
- Staartje linksonder.

Lettertype: standaard Avenir Next (staat op elke Mac, lijkt op TikTok's Proxima Nova).
Eigen font (bv. TikTok Sans of Proxima Nova) via --font-text / --font-header of de FONT_*-constanten.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

# ---------- fonts ----------
_FONT_DIR = Path(__file__).resolve().parent / "fonts"
_TIKTOK_SANS = _FONT_DIR / "TikTokSans.ttf"  # variabel font (OFL), github.com/tiktok/TikTokSans
FONT_WIDTH = 97  # breedte-as van TikTok Sans (100 = normaal; gemeten tegen het TikTok-voorbeeld)
# (pad, ttc-index, gewicht voor variabele fonts)
if _TIKTOK_SANS.exists():
    FONT_TEXT = (str(_TIKTOK_SANS), 0, 700)    # Bold
    FONT_HEADER = (str(_TIKTOK_SANS), 0, 600)  # SemiBold
else:  # fallback als de fontmap ontbreekt
    FONT_TEXT = ("/System/Library/Fonts/Avenir Next.ttc", 0, None)    # Bold
    FONT_HEADER = ("/System/Library/Fonts/Avenir Next.ttc", 2, None)  # Demi Bold


def _load_font(spec, size: int) -> ImageFont.FreeTypeFont:
    path, index, weight = spec
    f = ImageFont.truetype(path, size, index=index)
    if weight is not None:
        try:
            axes = f.get_variation_axes()
            vals = []
            for ax in axes:
                name = ax["name"].decode() if isinstance(ax["name"], bytes) else ax["name"]
                vals.append({"Weight": weight, "Optical size": ax["maximum"], "Slant": 0, "Width": FONT_WIDTH}
                            .get(name, ax["default"]))
            f.set_variation_by_axes(vals)
        except OSError:
            pass  # geen variabel font
    return f
# Emoji-font: de eerste die op deze computer staat. (pad, maat waarop hij scherp rendert)
# Apple = Mac (iPhone-look), Noto = Linux/Android-look, Segoe = Windows-look.
EMOJI_CANDIDATES = [
    ("/System/Library/Fonts/Apple Color Emoji.ttc", 160),
    ("/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf", 109),
    ("/usr/share/fonts/noto/NotoColorEmoji.ttf", 109),
    ("/usr/share/fonts/google-noto-emoji/NotoColorEmoji.ttf", 109),
    ("/usr/share/fonts/noto-emoji/NotoColorEmoji.ttf", 109),
    ("C:/Windows/Fonts/seguiemj.ttf", 160),
]
EMOJI_FONT, EMOJI_NATIVE = next(((p, n) for p, n in EMOJI_CANDIDATES if Path(p).exists()), EMOJI_CANDIDATES[0])

THEMES = {
    "light": {"bg": (255, 255, 255, 255), "header": (90, 90, 90, 255), "text": (0, 0, 0, 255),
              "avatar_bg": (206, 214, 220, 255), "avatar_fg": (105, 118, 133, 255)},
    # omgekeerd: zwarte bubbel, witte tekst (kleuren van wit gespiegeld)
    "invert": {"bg": (0, 0, 0, 255), "header": (165, 165, 165, 255), "text": (255, 255, 255, 255),
               "avatar_bg": (64, 68, 74, 255), "avatar_fg": (150, 160, 172, 255)},

}

# Maten op schaal 1.0 = afgestemd op een 1080 px brede video (overgenomen van het TikTok-voorbeeld)
BASE = {
    # alle maten gemeten op het TikTok-voorbeeld (pixels, baseline = onderkant van de letters)
    "width": 841,           # vaste bubbelbreedte; meer tekst loopt alleen naar beneden door
    "wrap_pad": 25,         # tekst breekt af op 25 px van de rechterrand (tekstvak 650, afgeleid uit het voorbeeld)
    "pad_left": 37,         # bubbelrand -> avatar
    "avatar": 100,
    "avatar_top": 77,       # bovenkant bubbel -> bovenkant avatar
    "gap": 27,              # avatar -> tekst
    "header_size": 38,      # kapitaalhoogte 26 px
    "text_size": 59,        # kapitaalhoogte 41 px, x-hoogte 30 px
    "first_baseline": 79,   # bovenkant bubbel -> baseline eerste kopregel
    "header_line": 62,      # baseline -> baseline binnen de kopregel
    "header_to_text": 78,   # baseline laatste kopregel -> baseline eerste commentregel
    "text_line": 74,        # baseline -> baseline binnen de comment
    "bottom": 63,           # baseline laatste commentregel -> onderkant bubbel
    "radius": 22,
    "tail_w": 50,
    "tail_h": 43,
    "shadow_blur": 16,
}
SHADOW_ALPHA = 60
SS = 3  # supersampling voor strakke randen


# ---------- tekst + emoji ----------
def _is_emoji_start(ch: str) -> bool:
    o = ord(ch)
    return (0x1F000 <= o <= 0x1FAFF or 0x2600 <= o <= 0x27BF or 0x2300 <= o <= 0x23FF
            or 0x2B00 <= o <= 0x2BFF or o in (0x00A9, 0x00AE, 0x203C, 0x2049, 0x2122, 0x2139, 0x3030, 0x303D))


def _is_emoji_cont(ch: str) -> bool:
    o = ord(ch)
    return o in (0xFE0F, 0x20E3, 0x200D) or 0x1F3FB <= o <= 0x1F3FF or 0xE0020 <= o <= 0xE007F


def _runs(text: str) -> list[tuple[bool, str]]:
    """Splits tekst in (is_emoji, stuk)-runs."""
    runs: list[tuple[bool, str]] = []
    i = 0
    while i < len(text):
        ch = text[i]
        if _is_emoji_start(ch):
            j = i + 1
            while j < len(text) and (_is_emoji_cont(text[j]) or (text[j - 1] == "‍" and _is_emoji_start(text[j]))):
                j += 1
            runs.append((True, text[i:j]))
            i = j
        else:
            j = i
            while j < len(text) and not _is_emoji_start(text[j]):
                j += 1
            runs.append((False, text[i:j]))
            i = j
    return runs


class _Typesetter:
    def __init__(self, font: ImageFont.FreeTypeFont, size: int):
        self.font = font
        self.size = size
        self.emoji_px = int(size * 1.045)
        self.emoji_lead = size * 0.02  # extra ruimte vóór een emoji naast de spatie (voorbeeld: 19 px van tekst tot emoji)
        try:
            self.emoji_font = ImageFont.truetype(EMOJI_FONT, EMOJI_NATIVE)
        except OSError:
            self.emoji_font = None

    def width(self, s: str) -> float:
        w = 0.0
        for is_e, part in _runs(s):
            w += (self.emoji_lead + self.emoji_px) if (is_e and self.emoji_font) else self.font.getlength(part)
        return w

    def _emoji_img(self, e: str) -> Image.Image:
        n = EMOJI_NATIVE
        im = Image.new("RGBA", (int(n * 1.4), int(n * 1.4)), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((0, 0), e, font=self.emoji_font, embedded_color=True)
        bbox = im.getbbox() or (0, 0, n, n)
        im = im.crop(bbox)
        return im.resize((self.emoji_px, int(self.emoji_px * im.height / max(1, im.width))), Image.LANCZOS)

    def draw(self, canvas: Image.Image, x: float, baseline: float, s: str, fill) -> None:
        d = ImageDraw.Draw(canvas)
        for is_e, part in _runs(s):
            if is_e and self.emoji_font:
                im = self._emoji_img(part)
                ey = int(baseline + self.size * 0.14 - im.height)  # emoji zakt iets onder de baseline
                canvas.alpha_composite(im, (int(x + self.emoji_lead), ey))
                x += self.emoji_lead + self.emoji_px
            else:
                d.text((x, baseline), part, font=self.font, fill=fill, anchor="ls")
                x += self.font.getlength(part)


def blur_name(canvas: Image.Image, tset, x: float, baseline: float, line: str, name: str) -> None:
    """Vervaagt de naam in een al getekende regel (privacy). Een regel die alleen uit (een deel van) de
    naam bestaat, wordt helemaal vervaagd."""
    if not name or not line.strip():
        return
    i = line.find(name)
    if i >= 0:
        x1, w = x + tset.width(line[:i]), tset.width(name)
    elif line.strip() in name:
        x1, w = x, tset.width(line)
    else:
        return
    asc, desc = tset.font.getmetrics()
    pad = tset.size * 0.12
    box = (int(x1 - pad), int(baseline - asc * 0.9 - pad), int(x1 + w + pad), int(baseline + desc * 0.6 + pad))
    canvas.paste(canvas.crop(box).filter(ImageFilter.GaussianBlur(tset.size * 0.2)), box)


def _wrap_words(text: str, ts: _Typesetter, max_w: float) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        if not words:
            lines.append("")
            continue
        cur = ""
        for w in words:
            trial = f"{cur} {w}" if cur else w
            if ts.width(trial) <= max_w or not cur:
                cur = trial
            else:
                lines.append(cur)
                cur = w
        lines.append(cur)
    # te lange losse woorden hard breken
    out: list[str] = []
    for line in lines:
        while ts.width(line) > max_w and len(line) > 1:
            cut = len(line) - 1
            while cut > 1 and ts.width(line[:cut]) > max_w:
                cut -= 1
            out.append(line[:cut])
            line = line[cut:]
        out.append(line)
    return out


def _wrap_header(name: str, ts: _Typesetter, max_w: float, template: str | None) -> list[str]:
    """Kopregel in blokken, zoals TikTok: 'Reply to' / naam / "'s comment"."""
    if template:
        return _wrap_words(template.format(user=name), ts, max_w)
    full = f"Reply to {name}'s comment"
    if ts.width(full) <= max_w:
        return [full]
    # past het niet op één regel, dan elk blok op een eigen regel (zoals TikTok)
    lines = ["Reply to"]
    lines.extend(_wrap_words(name, ts, max_w))
    lines.append("'s comment")
    return lines


def _truncate(lines: list[str], ts: _Typesetter, max_w: float, max_lines: int | None) -> list[str]:
    if not max_lines or len(lines) <= max_lines:
        return lines
    lines = lines[:max_lines]
    last = lines[-1]
    while last and ts.width(last + "…") > max_w:
        last = last[:-1]
    lines[-1] = last.rstrip() + "…"
    return lines


# ---------- avatar ----------
def _avatar(source: str | Path | None, size: int, colors: dict) -> Image.Image:
    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size - 1, size - 1), fill=255)
    if source and Path(source).exists():
        img = ImageOps.fit(Image.open(source).convert("RGBA"), (size, size), Image.LANCZOS)
    else:
        # standaard grijs profielicoon: hoofd (afgerond) + schouders
        img = Image.new("RGBA", (size, size), colors["avatar_bg"])
        d = ImageDraw.Draw(img)
        u = size / 100  # gemeten op een avatar van 100 px
        d.ellipse((31 * u, 23 * u, 68 * u, 64 * u), fill=colors["avatar_fg"])      # hoofd
        d.ellipse((15.5 * u, 70 * u, 83.5 * u, 138 * u), fill=colors["avatar_fg"])  # schouders
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


# ---------- bubbel ----------
def _bubble_shape(W: int, H: int, x0: int, y0: int, bw: int, bh: int, s: dict, tail: bool) -> Image.Image:
    shape = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(shape)
    d.rounded_rectangle((x0, y0, x0 + bw, y0 + bh), radius=s["radius"], fill=255)
    if tail:
        # hoek linksonder recht maken, dan staartje: linkerrand loopt door naar beneden,
        # punt licht afgerond, holle curve terug naar de onderrand
        d.rectangle((x0, y0 + bh - s["radius"], x0 + s["radius"], y0 + bh), fill=255)
        u = s["tail_h"] / 43  # vorm gemeten op het voorbeeld (staart 50 breed, 43 diep)
        bottom = y0 + bh
        rel = [(0, -1), (0, 40), (1, 42), (3, 43), (6, 42.5), (12, 40.5), (19, 37), (52, -1)]
        pts = [(x0 + rx * u, bottom + ry * u) for rx, ry in rel]
        d.polygon(pts, fill=255)
    return shape


def render_comment_reply(
    username: str,
    comment: str,
    avatar: str | Path | None = None,
    *,
    scale: float = 1.0,
    theme: str = "light",
    width: int | None = None,
    fit: bool = False,
    max_lines: int | None = None,
    header: str | None = None,
    shadow: bool = True,
    tail: bool = True,
    blur: bool = False,
    font_text: str | None = None,
    font_header: str | None = None,
) -> Image.Image:
    """
    Geeft een RGBA-afbeelding van de TikTok comment-reply bubbel terug.

    username     naam met of zonder @
    comment      commenttekst (emoji mag); \\n = harde regelbreuk
    avatar       pad naar profielfoto; zonder: grijs standaard-profielicoon
    scale        1.0 = juiste maat voor 1080 px brede video
    theme        "light" (standaard, wit) of "invert" (zwart met witte tekst)
    width        bubbelbreedte in px op schaal 1.0 (standaard 841, vast; tekst loopt naar beneden door)
    fit          True = bubbel krimpt mee bij korte tekst (standaard: vaste breedte)
    max_lines    comment afkappen met … na zoveel regels (standaard: nooit)
    header       eigen kopregel, bv. "Antwoord op de reactie van {user}"
    font_text    pad naar eigen font voor de comment (bv. TikTok Sans Bold)
    font_header  pad naar eigen font voor de kopregel
    """
    if theme == "dark":  # oude naam
        theme = "invert"
    if theme not in THEMES:
        raise ValueError(f"theme moet een van {list(THEMES)} zijn")
    colors = THEMES[theme]
    k = scale * SS
    s = {key: int(round(v * k)) for key, v in BASE.items()}
    if width:
        s["width"] = int(round(width * k))

    ft = _load_font((font_text, 0, None) if font_text else FONT_TEXT, s["text_size"])
    fh = _load_font((font_header, 0, None) if font_header else FONT_HEADER, s["header_size"])
    ts_text, ts_head = _Typesetter(ft, s["text_size"]), _Typesetter(fh, s["header_size"])

    name = username.strip().lstrip("@")
    text_x = s["pad_left"] + s["avatar"] + s["gap"]
    text_max = s["width"] - text_x - s["wrap_pad"]
    head_lines = _wrap_header(name, ts_head, text_max, header)
    body_lines = _truncate(_wrap_words(comment.strip(), ts_text, text_max), ts_text, text_max, max_lines)

    content_w = max([ts_head.width(l) for l in head_lines] + [ts_text.width(l) for l in body_lines])
    bw = s["width"]
    if fit:  # meekrimpen: rechtermarge zoals bij de breedste regel in het voorbeeld (44 px)
        bw = min(bw, int(text_x + content_w + 44 * k))

    # verticale layout op baselines, zoals gemeten in het voorbeeld
    last_head = s["first_baseline"] + (len(head_lines) - 1) * s["header_line"]
    last_body = last_head + s["header_to_text"] + (len(body_lines) - 1) * s["text_line"]
    bh = int(max(last_body + s["bottom"], s["avatar_top"] + s["avatar"] + s["pad_left"]))

    margin = s["shadow_blur"] * 2 if shadow else SS
    W = bw + 2 * margin
    H = bh + (s["tail_h"] if tail else 0) + 2 * margin
    x0 = y0 = margin
    canvas = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    shape = _bubble_shape(W, H, x0, y0, bw, bh, s, tail)

    if shadow:
        sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sh.putalpha(shape.point(lambda p: p * SHADOW_ALPHA // 255))
        sh = sh.filter(ImageFilter.GaussianBlur(s["shadow_blur"] / 2))
        canvas.alpha_composite(sh, (0, int(4 * k)) if 4 * k < H else (0, 0))
    canvas.paste(Image.new("RGBA", (W, H), colors["bg"]), (0, 0), shape)

    canvas.alpha_composite(_avatar(avatar, s["avatar"], colors), (x0 + s["pad_left"], y0 + s["avatar_top"]))

    # tekst
    for n, line in enumerate(head_lines):
        ts_head.draw(canvas, x0 + text_x, y0 + s["first_baseline"] + n * s["header_line"], line, colors["header"])
        if blur:
            blur_name(canvas, ts_head, x0 + text_x, y0 + s["first_baseline"] + n * s["header_line"], line, name)
    for n, line in enumerate(body_lines):
        ts_text.draw(canvas, x0 + text_x, y0 + last_head + s["header_to_text"] + n * s["text_line"], line, colors["text"])

    return canvas.resize((max(1, W // SS), max(1, H // SS)), Image.LANCZOS)


# ---------- video-overlay ----------
POSITIONS = {
    "top": ("(W-w)/2", "H*0.16"),
    "center": ("(W-w)/2", "(H-h)/2"),
    "upper-left": ("W*0.06", "H*0.16"),
}


def overlay_on_video(png: Path, video: Path, out: Path, start: float | None, end: float | None, position: str) -> None:
    x, y = POSITIONS.get(position, POSITIONS["top"])
    enable = ""
    if start is not None or end is not None:
        enable = f":enable='between(t,{start or 0},{end if end is not None else 1e9})'"
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(png),
        "-filter_complex", f"[0:v][1:v]overlay={x}:{y}{enable}[v]",
        "-map", "[v]", "-map", "0:a?", "-c:v", "libx264", "-crf", "18", "-preset", "medium",
        "-c:a", "copy", "-movflags", "+faststart", str(out),
    ], check=True)


def _video_width(video: Path) -> int:
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width",
                        "-of", "csv=p=0", str(video)], capture_output=True, text=True, check=True)
    return int(r.stdout.strip())


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="TikTok comment-reply bubbel renderen (PNG of over video).")
    p.add_argument("-u", "--username")
    p.add_argument("-c", "--comment")
    p.add_argument("-a", "--avatar", help="pad naar profielfoto (optioneel)")
    p.add_argument("-o", "--out", help="uitvoer .png, of .mp4 samen met --video")
    p.add_argument("--theme", choices=list(THEMES), default="light", help="light = wit (standaard), invert = zwart")
    p.add_argument("--invert", action="store_true", help="omgekeerd: zwarte bubbel met witte tekst")
    p.add_argument("--scale", type=float, help="standaard: videobreedte/1080, of 1.0 zonder video")
    p.add_argument("--width", type=int, help="bubbelbreedte op schaal 1.0 (standaard 841)")
    p.add_argument("--fit", action="store_true", help="bubbel laten meekrimpen bij korte tekst")
    p.add_argument("--max-lines", type=int)
    p.add_argument("--header", help='eigen kopregel, bv. "Antwoord op de reactie van {user}"')
    p.add_argument("--font-text", help="pad naar font voor de comment")
    p.add_argument("--font-header", help="pad naar font voor de kopregel")
    p.add_argument("--no-shadow", action="store_true")
    p.add_argument("--no-tail", action="store_true")
    p.add_argument("--blur-name", action="store_true", help="gebruikersnaam vervagen (privacy)")
    p.add_argument("--video")
    p.add_argument("--start", type=float)
    p.add_argument("--end", type=float)
    p.add_argument("--position", choices=list(POSITIONS), default="top")
    p.add_argument("--batch", help="JSON-bestand met een lijst van comments")
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
        img = render_comment_reply(
            job["username"], job["comment"], job.get("avatar"),
            scale=scale, theme=job.get("theme", "invert" if args.invert else args.theme), width=job.get("width", args.width), fit=job.get("fit", args.fit),
            max_lines=job.get("max_lines", args.max_lines), header=job.get("header", args.header),
            shadow=not args.no_shadow, tail=not args.no_tail, blur=job.get("blur_name", args.blur_name),
            font_text=job.get("font_text", args.font_text), font_header=job.get("font_header", args.font_header),
        )
        out = Path(job["out"])
        if video:
            png = out.with_suffix(".comment.png")
            img.save(png)
            overlay_on_video(png, video, out, job.get("start"), job.get("end"), job.get("position", args.position))
            print(f"✓ {out}  (bubbel: {png})")
        else:
            img.save(out)
            print(f"✓ {out}  ({img.width}×{img.height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
