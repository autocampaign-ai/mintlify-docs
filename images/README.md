# Screenshots and videos

Pages ship with **invisible placeholders** wherever a screenshot or video would help.
Customers see nothing until you add the file and uncomment the block. The full list
lives in [`MEDIA-CHECKLIST.md`](../MEDIA-CHECKLIST.md).

## What a placeholder looks like

```mdx
{/* MEDIA-TODO screenshot | /images/providers/twilio-connect.png
Capture: The Connect tab after credentials are saved, showing the Connected badge.
Route: /settings/channels
Redact: Account SID and Auth Token (show masked values only).
Publish: add the file at the path above, then delete this note and the comment markers around the Frame below. */}
{/*
<Frame caption="Connect tab with saved credentials">
  <img src="/images/providers/twilio-connect.png" alt="Twilio Connect tab showing masked credentials and a green Connected badge" />
</Frame>
*/}
```

## Adding a screenshot or video

1. Pick an item from `MEDIA-CHECKLIST.md` and open its page. Search for `MEDIA-TODO`.
2. Capture what the **Capture** line describes, starting from **Route**. For a video,
   follow the numbered **Script**.
3. Apply the **Redact** line. Use a demo workspace where you can.
4. Save the file at the exact path in the placeholder. Images go under `images/`,
   videos under `videos/`.
5. Delete the note comment. Remove the `{/*` and `*/}` lines around the `<Frame>`.
   Keep the caption and alt text unless the screen changed.
6. Run the checks, then open a pull request:

```bash
python3 scripts/media-checklist.py   # rebuilds the checklist and validates placeholders
mint broken-links                    # confirms every published image resolves
```

## Capture guidelines

- **Screenshots:** capture at 2x (retina), export PNG or WebP, and keep each file under 500 KB.
  Crop to the relevant UI, with no browser chrome. Use the light theme and English.
- **Videos:** MP4 (H.264), 1080p, no audio required, under 20 MB. Keep to the target
  length in the placeholder. For longer walkthroughs, host on YouTube or Loom and swap
  the `<video>` tag for an `<iframe>`, keeping the `title` attribute.
- **Alt text** describes what the image shows for someone who cannot see it. Update it
  if the screen differs from the description. Do not start with "Screenshot of".
- **Never publish** real customer data, phone numbers, API keys, tokens, or billing details.
- File names are kebab-case and already chosen in the placeholder. Do not rename them.

## Adding a new placeholder

Copy the format above exactly, since `scripts/media-checklist.py` parses it. Every note
needs `Capture:`, `Route:`, `Redact:`, and `Publish:` lines, and videos also need
`Script:`. Paths must be unique across the repo.
