---
name: comment-overlay
description: Render a realistic social comment as a transparent PNG or straight onto a video, for "reply to comment" ads and objection-handling videos. Covers the TikTok reply bubble, the Instagram comment card, the Instagram question sticker (Q&A, styles black, grey, purple, blue) and the Facebook comment (with or without a like). Use for "make a TikTok comment bubble", "reply to comment sticker", "Instagram comment overlay", "Instagram question sticker", "Facebook comment", "put this comment on the video", or when a script or brief opens with a customer comment on screen. Not for writing the comment or the hook itself (use `video-voorzet` or `title-hook-written`) and not for cutting the video (use `video-montage`).
---

# Comment overlay

Turns a comment (or a question and answer) into an overlay that looks like the real platform UI: same font, sizes,
line breaks, colours and shadow, calibrated pixel by pixel on screenshots of the apps. Output is a transparent PNG for
the editor, or a finished video with the overlay burned in. It serves the production step of the
[ad pipeline](../../references/ad-pipeline.md): after the script or brief, when a video opens with a customer comment.

Everything runs locally with the scripts in [scripts/](scripts/). The fonts ship with the skill in
[scripts/fonts/](scripts/fonts/) (TikTok Sans, Inter, Roboto, all OFL). Emoji come from the computer's own emoji
font: Apple Color Emoji on a Mac (the iPhone look), Noto Color Emoji on Linux (install `fonts-noto-color-emoji` if it
is missing), Segoe UI Emoji on Windows. On Linux and Windows the emoji therefore look like Android or Windows emoji,
not like iPhone emoji; render on a Mac when the iPhone look matters.

## Steps

1. **Get the content.** Ask for what is missing:
   - platform: TikTok, Instagram comment, Instagram question, or Facebook
   - the username (or name), and the comment text exactly as it should appear (keep the customer's spelling)
   - for a question sticker: the question and the answer, and a style
   - optional: a profile photo, a video to put it on, and when it appears and disappears (for example 0 to 3 s)
   Take real comments from the brand's research in Adflow or from the brief; never invent a "customer" comment and
   present it as real. If the user wants an invented one, say it is invented.

2. **Check the environment once.** `python3 -c "import PIL"` must work (else `pip3 install pillow`); for video also
   `ffmpeg -version`. Run the scripts from this skill's folder.

3. **Render.** Pick the script for the platform (table below). Without `--video` you get a PNG; with `--video in.mp4`
   you get the video with the overlay burned in, plus the PNG next to it. Size scales to the video width
   automatically (designed for 1080 px wide; 1080x1920 and 1080x1080 both work).

   ```bash
   python3 scripts/tiktok_comment.py -u "username" -c "Does this work on curly hair? 😊" -o comment.png
   python3 scripts/instagram_comment.py -u "username" -c "Does this work on curly hair? 🔥" -o comment.png
   python3 scripts/instagram_question.py -q "Does this work on curly hair?" -a "Yes, it does!" -o question.png
   python3 scripts/facebook_comment.py -n "First Last" -c "Does this work on curly hair?" --time 9h -o comment.png
   python3 scripts/tiktok_comment.py -u "username" -c "..." --video in.mp4 -o out.mp4 --start 0 --end 3
   ```

4. **Show the result** to the user (open the PNG or a frame of the video) and adjust on their feedback with the
   options below. Do not change the calibrated sizes in the scripts to "improve" the look.

5. **Hand over.** Put the PNG or video where the editor or the brief needs it (for example the brief board in
   Adflow, after the user agrees).

## Platforms and options

| Platform | Script | Default | Options |
|---|---|---|---|
| TikTok reply bubble | `tiktok_comment.py` | white, fixed width, text flows down | `--invert` (black), `--avatar`, `--header "..."` (own header line, `{user}` = name), `--max-lines`, `--fit` (shrink for short text) |
| Instagram comment | `instagram_comment.py` | white, shrinks to fit, full width once the text wraps | `--invert`, `--avatar`, `--sub "..."` (own "Replying to" line), `--fixed`, `--max-lines` |
| Instagram question sticker | `instagram_question.py` | style `black` | `--style black\|grey\|purple\|blue` |
| Facebook comment | `facebook_comment.py` | with like (1 and blue thumb), shrinks to fit; on a video it gets a white card behind it so "Like · Reply" stays readable | `--no-like`, `--likes 12`, `--time 45m`, `--avatar`, `--invert` (dark mode), `--background` (white card on a PNG too), `--transparent` (no card on video) |

Shared options: `--video`, `--start`, `--end`, `--position top|center|upper-left`, `--scale`, `--no-shadow` (Instagram
and Facebook), and `--batch file.json` for many at once: a JSON list of objects with the same fields
(`username`/`name`, `comment` or `question`/`answer`, `out`, optional `video`, `start`, `end`, `theme`, `style`).

Without `--avatar` every platform shows its own grey default profile icon.

## Output

One PNG per comment (transparent background, ready for any editor) or an `.mp4` with the overlay burned in, plus a
short line to the user with the file paths and what to check: spelling of the comment, the name, and the timing on
the video. Next step: the editor places the PNG, or the video goes to review.
