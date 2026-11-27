---
name: video-montage
description: Edit rough video ad variants yourself (9:16, on-screen text and music) from creator footage that is in Adflow, without downloading the source clips. Finds moments in the asset's per-second analysis (visual description and on-screen text), judges the image on the frame captures, gets a storyboard approved first, renders with ffmpeg straight from the Adflow video URLs, adds royalty-free music and uploads to the brief board after approval. Use for "generate the videos", "edit this yourself", "make the edit", "render the variants", or when the user wants Claude to produce the videos after an editor brief. Video with existing footage only; not for writing the brief (use video-brief) or a shotlist for new footage (use broll-shotlist).
---

# Video montage (after S6, video)

After the **editor brief** (S6, `video-brief`) Claude edits the variants itself from the footage on the brief board.
The result is a **rough edit that can launch**; an editor can still polish timing, typography and colour. Pipeline:
[ad-pipeline.md](../../references/ad-pipeline.md).

> **Core:** don't download source clips. For each video Adflow has a **per-second analysis** (visual description and
> on-screen text with timestamps, plus cuts), a light transcode (1080×1920) and **frame captures at 1 per second
> (frame N = second N)**. Find moments in the analysis, judge the image on the frames, render with ffmpeg straight
> from the URL. Only the exports are stored locally.

Requires on the machine: `ffmpeg`, `curl` and Python with Pillow. The script is
[scripts/montage.py](scripts/montage.py).

## Input (read first)
- **Approved script and on-screen text** per hook and the shared body (from the editor brief or the concept).
- **Footage:** the board of the creator brief, plus any extra assets the user adds to the brief.
- **Work folder:** a folder in the user's project (ask if unclear; never `/tmp`). Only exports and storyboards go
  there; source clips stay in Adflow.

## Steps (one step per turn, stop at every choice)

1. **Map the footage.** List the assets on the board and read each asset's details: transcode URL, duration and
   frame captures (the frame key is the part before `_thumb.` in the frame URL). Don't trust the asset's summary
   description or tags at the top: they are often wrong (wrong occasion, "speaks" on silent clips). The audio
   check on the asset (speech or only music) is reliable. Put the clips in a `spec.json` (format in the script).

2. **Find moments in the per-second analysis (first).** Read each clip's segments: per second a visual description
   and on-screen text, plus the detected cuts. You can also search within one clip ("hand pours"). Pick candidate
   moments to the second. This works without a terminal too.
   - Status **missing** (shot scan pending) means the clip was not analysed, and there is no way to start that from
     Claude. Fall back to the frames.
   - Cut detection can miss a cut within the same setting; check it on the frames.

3. **Judge the image on the frames.** The analysis says nothing about sharpness, composition or light. Look at the
   candidates: `python3 -I scripts/montage.py spec.json frames [step]` gives a contact sheet per clip with second
   labels. For many or long clips start with step 3, then only the relevant parts.
   - Judge at **full frame size (320×568)**: text, text versus faces, composition and obvious blur are visible there.
     At ±120 px wide they are not. For slight blur or small print, grab a bigger frame from the video
     (`ffmpeg -ss <t> -i <url> -frames:v 1`).
   - Claude scales large images down by itself, so several small sheets work better than one huge grid.

4. **Choose shots** (rules from earlier edits):
   - Length ±15–17 s; shots up to ±2 s; a shot with text at least ±2 s so it can be read.
   - **Never text over a face:** on shots with a person use `pos: "low"` (60%, on the torso), otherwise `"high"` (22%).
   - **Text style.** Default is dark text on white boxes. For a **TikTok-native edit** (text in the style of the
     TikTok/Reels "Classic" text: white TikTok Sans, dark outline, no box, centred) set `"text_style": "tiktok"` in
     the spec. Positions are then `mid` (45%, default), `upper`, `top` and `low`. Ask which style the user wants when
     the brief or reference does not make it clear.
   - **Safe zone (9:16, 1080×1920).** Important text **and** image (product, face, payoff) stay inside
     x 73–1029 and y 283–1533; in the lower right (from y 862) the platform buttons sit, so there x stays ≤ 887 (centred text may reach 90 px further so lines stay wide).
     Top and bottom matter most. Text always stays centred on the frame; the script wraps it narrower where needed to stay inside the zone, warns when a card still leaves
     it, and draws the zone as a red outline on storyboard stills. No room above a product? Give the shot a 6th
     field `zoom` (for example `1.3`): it zooms in from the top so the product moves down and the text fits above it.
   - **No clip twice** in one variant, and repeat the same setting (the same stand or table) as little as possible.
   - **Hooks differ in image too.** Only use a hook that promises a reaction if the reaction is really on screen.
   - **No blurred shots under important text.** Prefer a sharp detail or close-up.
   - **Text fits the image:** put the payoff on the image that proves it (for example "every morning" on morning
     light with the product in use).

5. **Storyboard and approval (always before rendering).**
   `python3 -I scripts/montage.py spec.json storyboard` gives one still per shot with text, source clip and duration.
   Before you show it, check it at full size for blur, text over faces and repeated settings. Send it and stop.
   - If the user dislikes a shot: make an options sheet with 3–4 alternatives, text already on them, and give your
     pick. Point out duplicate shots and repeats across variants yourself.
   - When the user changes text, change it in the editor brief too.

6. **Render.** `python3 -I scripts/montage.py spec.json render` gives `exports/<name>-V1.mp4` and so on, straight
   from the URLs (±1.5 s per shot). Spot-check frames from the export (text, faces, order) before you send it.
   Black bars the user sees usually come from the player; check the file (1080×1920, square pixels) before you
   change anything.

7. **Music.** Adflow usually only holds voice-overs, and commercial songs may not run under paid ads. Ask: generate
   or supplied by the user (a library with an ad licence, or the platform's own sound collection).
   - Generate an instrumental track of the video length plus 1 s (for example ElevenLabs Music). **Check the cost
     first.** Let the user listen to the track.
   - `python3 -I scripts/montage.py spec.json music <track.mp3>` gives `-music.mp4` files with fade in, a 1.2 s fade
     out and loudness at −16 LUFS.

8. **Deliver (only after approval).** Upload the exports to the **board of the editor brief** and check that they
   are there with the right size. Note the asset IDs. Clean up locally only when the user says so. Launching is a
   separate step, only on explicit request.

## Honest about the gain
The per-second analysis makes finding moments easiest: image and text per second, without fetching anything. Frames
and cutting straight from the URL also save **downloading, disk space, storage questions and clean-up**. The job
does **not get noticeably faster in minutes**: most time goes into feedback rounds on shots and text. Don't claim a
speed-up factor.

## Known pitfalls
- A new brief document can drop the paragraph directly after a heading. Read the brief back and restore missing lines.
- Python `urllib` can fail on the CDN certificates. Use `curl` for frames and downloads.
- Homebrew `ffmpeg` has no `drawtext`. Text cards are PNG overlays (built into the script).
- The written hook in the hook analysis can be "unknown" while the segments do contain the text; use the segments.
- Workspace search does not find moments (it sorts by date); search within one clip's segments instead.
- Frame and transcode URLs carry a version code (`?v=`). Fetch them again after a new upload.

## Output
Per step: the image or file sent to the user with a short note, then stop for approval. No long explanations.
After step 8 the user can launch the variants from the concept.
