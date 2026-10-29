# Draws assets/og-preview.webp. Rerun after the name, headline or location changes on index.html.
# Needs macOS for Helvetica Neue, and Pillow with WebP support.
from PIL import Image, ImageDraw, ImageFont

OUT = "assets/og-preview.webp"
W, H = 1200, 630
BG, FG, MUTED, LINK = "#fefefa", "#1b1d1f", "#5a6068", "#2c5a8c"
TTC = "/System/Library/Fonts/HelveticaNeue.ttc"

MARGIN = 96
MARK_SIZE = 96
NAME_BASELINE = 300
HEADLINE_BASELINE = 384
FOOTER_BASELINE = H - MARGIN


# HelveticaNeue.ttc index 1 is Bold, 0 is Regular.
def bold(size):
    return ImageFont.truetype(TTC, size, index=1)


def regular(size):
    return ImageFont.truetype(TTC, size, index=0)


img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

mark = (MARGIN, MARGIN, MARGIN + MARK_SIZE, MARGIN + MARK_SIZE)
d.rounded_rectangle(mark, radius=18, fill=LINK)
d.text(
    (MARGIN + MARK_SIZE // 2, MARGIN + MARK_SIZE // 2),
    "DD",
    font=bold(42),
    fill=BG,
    anchor="mm",
)

d.text((MARGIN, NAME_BASELINE), "Daniel Dutra", font=bold(96), fill=FG, anchor="ls")
d.text(
    (MARGIN, HEADLINE_BASELINE),
    "Full-stack developer",
    font=regular(56),
    fill=FG,
    anchor="ls",
)
d.text(
    (MARGIN, FOOTER_BASELINE),
    "Toronto, Canada",
    font=regular(36),
    fill=MUTED,
    anchor="ls",
)
d.text(
    (W - MARGIN, FOOTER_BASELINE),
    "dandutra.github.io",
    font=regular(36),
    fill=LINK,
    anchor="rs",
)

img.save(OUT, "WEBP", quality=90, method=6)
print(f"Wrote {OUT}")
