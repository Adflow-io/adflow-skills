#!/usr/bin/env python3
"""
Instagram vraag-sticker (Q&A) — herbruikbaar component.

Kaart met gekleurde kop (de vraag, gecentreerd) en witte body (het antwoord, groot en vet, gecentreerd).
Vaste breedte; langere vraag of antwoord loopt naar beneden door.

Stijlen: black (standaard), grey, purple (paars→roze verloop), blue (blauw verloop).

Gebruik als module:
    from instagram_question import render_instagram_question
    render_instagram_question("Dit is een korte vraag", "Kort antwoord").save("q.png")

Gebruik als CLI:
    python3 scripts/instagram_question.py -q "Werkt dit ook bij krullend haar?" -a "Ja, juist!" -o q.png
    python3 scripts/instagram_question.py -q "..." -a "..." --style purple -o q.png
    python3 scripts/instagram_question.py -q "..." -a "..." --video in.mp4 -o out.mp4 --start 0 --end 3
    python3 scripts/instagram_question.py --batch vragen.json   # lijst van {"question","answer","out","style"?}

Let op: maten zijn afgelezen van screenshots (niet pixel-exact gemeten); lettertype en
regelbreedtes zijn wel gemeten. Lettertype: Inter (scripts/fonts/Inter.ttf, OFL).
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, str(Path(__file__).resolve().parent))
from instagram_comment import INTER, SHADOWS, _IGType  # noqa: E402
from instagram_comment import _card  # noqa: E402
from tiktok_comment import POSITIONS, SS, _video_width, _wrap_words, overlay_on_video  # noqa: E402

# 1.0 = juiste maat voor 1080 px brede video (kaart van 600 → ~860 px, zelfde gevoel als de comment-kaarten)
VIDEO_SCALE = 1.43

STYLES = {
    "black":  {"head": [(38, 38, 38)],                     "q": (255, 255, 255)},
    "grey":   {"head": [(239, 239, 239)],                  "q": (128, 128, 128)},
    "purple": {"head": [(122, 52, 234), (226, 82, 114)],   "q": (255, 255, 255)},
    "blue":   {"head": [(76, 150, 178), (134, 210, 234)],  "q": (255, 255, 255)},
}
ANSWER_COLOR = (38, 38, 38, 255)
BODY_COLOR = (255, 255, 255, 255)

BASE = {
    "width": 600,
    "radius": 30,
    "q_size": 28.9,      # Inter SemiBold, tekst-optiek
    "q_line": 40,        # regelafstand vraag
    "q_pad": 26.5,       # boven/onder in de kop (rond de regelbox)
    "q_box": 500,        # maximale tekstbreedte vraag
    "a_size": 40.3,      # Inter SemiBold, tekst-optiek
    "a_line": 47,        # regelafstand antwoord
    "a_pad": 51.5,       # boven/onder in de body (rond de regelbox)
    "a_min": 177,        # minimale bodyhoogte (1 regel antwoord)
    "a_box": 500,        # maximale tekstbreedte antwoord
}


def _font(size: float, weight: int) -> ImageFont.FreeTypeFont:
    f = ImageFont.truetype(str(INTER), size)
    f.set_variation_by_axes([14, weight])  # tekst-optiek, past op de gemeten regelbreedtes
    return f


def _gradient(w: int, h: int, colors: list[tuple]) -> Image.Image:
    if len(colors) == 1:
        return Image.new("RGBA", (w, h), colors[0] + (255,))
    (r1, g1, b1), (r2, g2, b2) = colors
    row = Image.new("RGBA", (w, 1))
    px = row.load()
    for x in range(w):
        t = x / max(1, w - 1)
        px[x, 0] = (round(r1 + (r2 - r1) * t), round(g1 + (g2 - g1) * t), round(b1 + (b2 - b1) * t), 255)
    return row.resize((w, h))


def _centered_block(canvas, tset: _IGType, lines, cx, top, line_h, fill):
    """Regels gecentreerd; 'top' = bovenkant van de eerste regelbox."""
    asc, desc = tset.font.getmetrics()
    for n, line in enumerate(lines):
        w = tset.width(line)
        # baseline midden in de regelbox, zoals CSS line-height doet
        baseline = top + n * line_h + (line_h - (asc + desc)) / 2 + asc
        tset.draw(canvas, cx - w / 2, baseline, line, fill)


def render_instagram_question(
    question: str,
    answer: str,
    *,
    style: str = "black",
    scale: float = 1.0,
    shadow: bool = True,
) -> Image.Image:
    if style not in STYLES:
        raise ValueError(f"style moet een van {list(STYLES)} zijn")
    st = STYLES[style]
    k = scale * VIDEO_SCALE * SS
    s = {key: v * k for key, v in BASE.items()}

    tq = _IGType(_font(s["q_size"], 600), s["q_size"])
    ta = _IGType(_font(s["a_size"], 600), s["a_size"])
    q_lines = _wrap_words(question.strip(), tq, s["q_box"])
    a_lines = _wrap_words(answer.strip(), ta, s["a_box"])

    head_h = 2 * s["q_pad"] + len(q_lines) * s["q_line"]
    body_h = max(s["a_min"], 2 * s["a_pad"] + len(a_lines) * s["a_line"])
    bw, bh = int(s["width"]), int(head_h + body_h)

    canvas, m = _card(bw, bh, int(s["radius"]), k, BODY_COLOR, shadow)
    # kop: verloop/kleur, alleen bovenhoeken afgerond (masker = kaartvorm ∩ kopstrook)
    head = _gradient(bw, int(head_h), st["head"])
    mask = Image.new("L", (bw, int(head_h)), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=int(s["radius"]), fill=255)
    canvas.paste(head, (m, m), mask)

    cx = m + bw / 2
    _centered_block(canvas, tq, q_lines, cx, m + s["q_pad"], s["q_line"], st["q"] + (255,))
    a_top = m + head_h + (body_h - len(a_lines) * s["a_line"]) / 2
    _centered_block(canvas, ta, a_lines, cx, a_top, s["a_line"], ANSWER_COLOR)
    return canvas.resize((max(1, canvas.width // SS), max(1, canvas.height // SS)), Image.BOX)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Instagram vraag-sticker renderen (PNG of over video).")
    p.add_argument("-q", "--question")
    p.add_argument("-a", "--answer")
    p.add_argument("-o", "--out")
    p.add_argument("--style", choices=list(STYLES), default="black")
    p.add_argument("--scale", type=float, help="standaard: videobreedte/1080, of 1.0 zonder video")
    p.add_argument("--no-shadow", action="store_true")
    p.add_argument("--video")
    p.add_argument("--start", type=float)
    p.add_argument("--end", type=float)
    p.add_argument("--position", choices=list(POSITIONS), default="top")
    p.add_argument("--batch")
    args = p.parse_args(argv)

    if args.batch:
        jobs = json.loads(Path(args.batch).read_text())
    else:
        if not (args.question and args.answer and args.out):
            p.error("--question, --answer en --out zijn verplicht (of gebruik --batch)")
        jobs = [{"question": args.question, "answer": args.answer, "out": args.out,
                 "video": args.video, "start": args.start, "end": args.end}]
    for job in jobs:
        video = Path(job["video"]) if job.get("video") else None
        scale = job.get("scale") or args.scale or (_video_width(video) / 1080 if video else 1.0)
        img = render_instagram_question(job["question"], job["answer"], style=job.get("style", args.style),
                                        scale=scale, shadow=not args.no_shadow)
        out = Path(job["out"])
        if video:
            png = out.with_suffix(".question.png")
            img.save(png)
            overlay_on_video(png, video, out, job.get("start"), job.get("end"), job.get("position", args.position))
            print(f"✓ {out}  (sticker: {png})")
        else:
            img.save(out)
            print(f"✓ {out}  ({img.width}×{img.height})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
