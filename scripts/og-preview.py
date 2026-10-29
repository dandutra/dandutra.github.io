# Draws assets/og-preview.webp. Rerun after the name, headline or location changes on index.html.
# Needs macOS (Helvetica Neue) and Pillow with WebP support. Run from the repo root: python3 scripts/og-preview.py
from PIL import Image, ImageDraw, ImageFont

OUT = "assets/og-preview.webp"
W, H = 1200, 630
BG, FG, MUTED, LINK = "#fefefa", "#1b1d1f", "#5a6068", "#2c5a8c"
TTC = "/System/Library/Fonts/HelveticaNeue.ttc"

# HelveticaNeue.ttc index 1 is Bold, 0 is Regular.
bold = lambda s: ImageFont.truetype(TTC, s, index=1)
regular = lambda s: ImageFont.truetype(TTC, s, index=0)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)
x = 96

d.rounded_rectangle((x, 96, x + 96, 192), radius=18, fill=LINK)
d.text((x + 48, 144), "DD", font=bold(42), fill=BG, anchor="mm")

d.text((x, 300), "Daniel Dutra", font=bold(96), fill=FG, anchor="ls")
d.text((x, 384), "Full-stack developer", font=regular(56), fill=FG, anchor="ls")
d.text((x, 534), "Toronto, Canada", font=regular(36), fill=MUTED, anchor="ls")
d.text((W - x, 534), "dandutra.github.io", font=regular(36), fill=LINK, anchor="rs")

img.save(OUT, "WEBP", quality=90, method=6)
print(f"Wrote {OUT}")
