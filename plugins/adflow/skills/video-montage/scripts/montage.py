#!/usr/bin/env python3
"""Rough ad edit from footage in Adflow, without downloading the source clips.

Usage:
  python3 -I montage.py <spec.json> frames [step]   # contact sheets from Adflow frame captures (1 frame/sec)
  python3 -I montage.py <spec.json> storyboard      # 1 still per shot + on-screen text -> storyboard.jpg (get approval first!)
  python3 -I montage.py <spec.json> render [V1 V2]  # render variants straight from the transcode URLs
  python3 -I montage.py <spec.json> music <track>   # put music under every render (fade in/out, loudnorm)

spec.json:
{
  "name": "brand-concept",             # prefix for the exports
  "out_dir": "/path/to/work/folder",   # exports and storyboard go here; source clips do not
  "clips": {                           # short name -> Adflow quality transcode URL (+ frame key for 'frames')
    "Received": {"url": "https://cdn.adflow.io/public/transcoded/<key>_quality.mp4", "frames": "<key>", "duration": 17.4}
  },
  "hooks": {"V1": ["Received", 0.3, 2.2, "Hook text", "low"]},
  "body":  [["Received", 6.3, 1.4, null], ["Product", 4.0, 2.2, "On-screen text"]]
}
Shot = [clip, start_sec, duration_sec, text|null, pos, zoom] with pos "high" (22%, default) or "low" (60%, below faces).

Optional "text_style" in spec.json:
  "boxed"  (default) dark text on white rounded boxes, Avenir Next.
  "tiktok" white TikTok Sans (bold) with a dark outline, no box, centred like the TikTok/Reels "Classic" text.
           pos: "mid" (45%, default), "upper" (20%), "top" (30%), "low" (66%). "high" counts as "upper".
           Emoji are drawn in colour (Apple Color Emoji on macOS). A warning is printed when a card leaves the
           Reels safe zone (top 270 px and bottom 670 px kept free).
Optional zoom (6th shot field, e.g. 1.3): zooms in from the top edge, so the subject moves down in the frame. Use it
to make room above a product for text that must stay out of the top safe zone.
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))

W, H = 1080, 1920
FONT_PATH = "/System/Library/Fonts/Avenir Next.ttc"
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

def font(size=62):
    try: return ImageFont.truetype(FONT_PATH, size, index=2)  # Avenir Next Demi Bold (macOS); falls back to Arial Bold
    except Exception: return ImageFont.truetype(BOLD, size)

FONT = font()

def wrap(d, text, maxw=860):
    """Fewest lines; with 2 lines, split as evenly as possible (no orphan word)."""
    if d.textlength(text, font=FONT) <= maxw: return [text]
    w = text.split(); best = None
    for i in range(1, len(w)):
        a, b = " ".join(w[:i]), " ".join(w[i:])
        m = max(d.textlength(a, font=FONT), d.textlength(b, font=FONT))
        if m <= maxw and (best is None or m < best[0]): best = (m, [a, b])
    if best: return best[1]
    lines, cur = [], ""
    for x in w:
        t = (cur + " " + x).strip()
        if d.textlength(t, font=FONT) <= maxw: cur = t
        else: lines.append(cur); cur = x
    return lines + [cur]

def card(text, path, pos="high"):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    y = int(H * (0.60 if pos == "low" else 0.22)); lh, pad = 84, 26
    for ln in wrap(d, text):
        tw = d.textlength(ln, font=FONT); x = (W - tw) / 2
        d.rounded_rectangle([x - pad, y - 10, x + tw + pad, y + lh - 4], radius=18, fill=(255, 255, 255, 240))
        d.text((x, y), ln, font=FONT, fill=(20, 20, 20, 255)); y += lh + 6
    img.save(path); return path

TT_FONT_PATH = os.path.join(HERE, "fonts", "TikTokSans.ttf")
EMOJI_PATH = "/System/Library/Fonts/Apple Color Emoji.ttc"
TT_POS = {"mid": 0.45, "upper": 0.20, "high": 0.20, "top": 0.30, "low": 0.66}
SAFE_TOP, SAFE_BOTTOM = 270, H - 670   # Reels: keep the top 14% and bottom 35% free of text

def tt_font(size=84):
    f = ImageFont.truetype(TT_FONT_PATH, size)
    f.set_variation_by_axes([36, 100, 740, 0])   # opsz, width, weight (bold), slant
    return f

def is_emoji(ch): return ord(ch) >= 0x1F000 or 0x2190 <= ord(ch) <= 0x2BFF

def tt_card(text, path, pos="mid"):
    """White TikTok Sans with a 4 px dark outline, centred, colour emoji; same wrapping as the boxed style."""
    global FONT
    f = tt_font(); old = FONT; FONT = f
    text = text.replace("\ufe0f", "")
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    try: lines = wrap(d, text, maxw=900)
    finally: FONT = old
    try: emo_font = ImageFont.truetype(EMOJI_PATH, 160)
    except Exception: emo_font = None
    lh = 92; y0 = int(H * TT_POS.get(pos, 0.45)) - len(lines) * lh // 2
    emw = 80
    def width(s): return sum(emw if is_emoji(c) else d.textlength(c, font=f) for c in s)
    for i, ln in enumerate(lines):
        x = (W - width(ln)) / 2; y = y0 + i * lh
        for ch in ln:
            if is_emoji(ch):
                if emo_font:
                    e = Image.new("RGBA", (180, 180), (0, 0, 0, 0))
                    ImageDraw.Draw(e).text((0, 0), ch, font=emo_font, embedded_color=True)
                    if e.getbbox(): img.alpha_composite(e.crop(e.getbbox()).resize((72, 72)), (int(x + 6), int(y + 12)))
                x += emw
            else:
                d.text((x, y), ch, font=f, fill=(255, 255, 255, 255), stroke_width=4, stroke_fill=(30, 30, 30, 255))
                x += d.textlength(ch, font=f)
    box = img.split()[3].getbbox()
    if box and (box[1] < SAFE_TOP or box[3] > SAFE_BOTTOM):
        print(f"WARNING: text '{text}' at y {box[1]}-{box[3]} leaves the safe zone ({SAFE_TOP}-{SAFE_BOTTOM}).")
    img.save(path); return path

VF = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1"

def zoom_vf(z):
    w, h = int(W * z) // 2 * 2, int(H * z) // 2 * 2
    return f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={W}:{H}:(iw-{W})/2:0,fps=30,setsar=1"

def seg(spec, tmp, tag, shot, still=False):
    clip, ss, dur, text = shot[:4]
    tiktok = spec.get("text_style") == "tiktok"
    pos = shot[4] if len(shot) > 4 and shot[4] else ("mid" if tiktok else "high")
    vf = zoom_vf(float(shot[5])) if len(shot) > 5 and shot[5] else VF
    make_card = tt_card if tiktok else card
    url = spec["clips"][clip]["url"]
    t = ss + dur * 0.6 if still else ss
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(t)] + ([] if still else ["-t", str(dur)]) + ["-i", url]
    if text:
        cmd += ["-i", make_card(text, f"{tmp}/{tag}.png", pos), "-filter_complex",
                f"[0:v]{vf}[v];[v][1:v]overlay=0:0,format=yuv420p[o]", "-map", "[o]"]
    else:
        cmd += ["-vf", vf + ",format=yuv420p"]
    out = f"{tmp}/{tag}.{'jpg' if still else 'mp4'}"
    cmd += (["-frames:v", "1", "-update", "1"] if still else ["-an", "-c:v", "libx264", "-preset", "medium", "-crf", "18"]) + [out]
    subprocess.run(cmd, check=True); return out

def label_sheet(items, cols, title, path, cw=290):
    ch = 545; rows = (len(items) + cols - 1) // cols
    img = Image.new("RGB", (cols * cw + 10, rows * ch + 50), "white"); d = ImageDraw.Draw(img)
    d.text((10, 12), title, fill="black", font=ImageFont.truetype(BOLD, 22))
    f = ImageFont.truetype(BOLD, 17)
    for k, (p, lab) in enumerate(items):
        im = Image.open(p).convert("RGB").resize((270, 480)); x = 10 + (k % cols) * cw; y = 50 + (k // cols) * ch
        img.paste(im, (x, y)); d.text((x, y + 486), f"{k+1}. {lab}", fill="black", font=f)
    img.save(path, quality=88); return path

def main():
    spec = json.load(open(sys.argv[1])); mode = sys.argv[2]; rest = sys.argv[3:]
    out = spec["out_dir"]; tmp = f"{out}/tmp"; os.makedirs(tmp, exist_ok=True)
    name = spec["name"]

    if mode == "frames":
        # Adflow frame captures: 1 per second, frame N = second N. curl, because Python SSL can fail on the CDN certs.
        cfg = f"{tmp}/frames.cfg"
        with open(cfg, "w") as c:
            for clip, info in spec["clips"].items():
                os.makedirs(f"{tmp}/frames/{clip}", exist_ok=True)
                n = int(info["duration"]) + 1
                for i in range(n):
                    c.write(f'url = "https://cdn.adflow.io/public/thumbnails/{info["frames"]}_thumb.{i:07d}.jpg"\n'
                            f'output = "{tmp}/frames/{clip}/{i:03d}.jpg"\n')
        subprocess.run(["curl", "-sS", "--parallel", "--parallel-max", "16", "-K", cfg])
        step = int(rest[0]) if rest else 1   # for long clips start coarse, e.g. 3 = every 3rd second
        fnt = ImageFont.truetype(BOLD, 16)
        for clip in spec["clips"]:
            fs = sorted(f for f in os.listdir(f"{tmp}/frames/{clip}") if f.endswith(".jpg"))[::step]
            w, h = 120, 213; cols = min(12, len(fs)); rows = (len(fs) + cols - 1) // cols
            s = Image.new("RGB", (cols * w, rows * (h + 20)), "white"); d = ImageDraw.Draw(s)
            for k, fn in enumerate(fs):
                x = (k % cols) * w; y = (k // cols) * (h + 20)
                s.paste(Image.open(f"{tmp}/frames/{clip}/{fn}").convert("RGB").resize((w, h)), (x, y))
                d.text((x + 3, y + h + 1), f"{int(fn[:3])}s", fill="black", font=fnt)
            s.save(f"{out}/frames-{clip}.jpg", quality=85); print(f"{out}/frames-{clip}.jpg")
        return

    if mode == "storyboard":
        items = [(seg(spec, tmp, f"hook{v}", h, still=True), f"HOOK {v} · {h[2]}s") for v, h in spec["hooks"].items()]
        items += [(seg(spec, tmp, f"b{i:02d}", b, still=True), f"{b[0]} · {b[2]}s") for i, b in enumerate(spec["body"])]
        total = list(spec["hooks"].values())[0][2] + sum(b[2] for b in spec["body"])
        p = label_sheet(items, 6, f"Storyboard · ±{total:.1f}s · hooks first, then the shared body", f"{out}/storyboard.jpg")
        print(p); return

    if mode == "render":
        os.makedirs(f"{out}/exports", exist_ok=True)
        body = [seg(spec, tmp, f"b{i:02d}", b) for i, b in enumerate(spec["body"])]
        for v, h in spec["hooks"].items():
            if rest and v not in rest: continue
            lst = f"{tmp}/{v}.txt"
            with open(lst, "w") as f:
                for p in [seg(spec, tmp, f"hook{v}", h)] + body: f.write(f"file '{p}'\n")
            o = f"{out}/exports/{name}-{v}.mp4"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy",
                            "-movflags", "+faststart", o], check=True); print(o)
        return

    if mode == "music":
        track = rest[0]
        for fn in sorted(os.listdir(f"{out}/exports")):
            if not fn.endswith(".mp4") or fn.endswith("-music.mp4"): continue
            i = f"{out}/exports/{fn}"
            d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", i],
                                     capture_output=True, text=True).stdout)
            o = i[:-4] + "-music.mp4"
            af = f"[1:a]atrim=0:{d},asetpts=PTS-STARTPTS,afade=t=in:d=0.15,afade=t=out:st={d-1.2:.2f}:d=1.2,loudnorm=I=-16:TP=-1.5:LRA=11[a]"
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", i, "-i", track, "-filter_complex", af, "-map", "0:v",
                            "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                            "-movflags", "+faststart", o], check=True); print(o)
        return
    sys.exit(__doc__)

if __name__ == "__main__":
    main()
