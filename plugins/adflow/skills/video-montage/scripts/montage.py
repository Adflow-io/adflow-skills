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
Shot = [clip, start_sec, duration_sec, text|null, pos] with pos "high" (22%, default) or "low" (60%, below faces).
"""
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

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

VF = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1"

def seg(spec, tmp, tag, shot, still=False):
    clip, ss, dur, text = shot[:4]; pos = shot[4] if len(shot) > 4 else "high"
    url = spec["clips"][clip]["url"]
    t = ss + dur * 0.6 if still else ss
    cmd = ["ffmpeg", "-v", "error", "-y", "-ss", str(t)] + ([] if still else ["-t", str(dur)]) + ["-i", url]
    if text:
        cmd += ["-i", card(text, f"{tmp}/{tag}.png", pos), "-filter_complex",
                f"[0:v]{VF}[v];[v][1:v]overlay=0:0,format=yuv420p[o]", "-map", "[o]"]
    else:
        cmd += ["-vf", VF + ",format=yuv420p"]
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
