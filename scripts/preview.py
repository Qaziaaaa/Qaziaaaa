import build_banner as B
import re
import os

B.PHOTO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "profile.jpg")

img = B.load_and_crop()
gray = B.ascii_gray(img)
mask = B.segment_mask(img)
cells = B.ascii_cells(gray, mask)


def strip(svg):
    svg = re.sub(r"<animate[^>]*/>", "", svg)
    svg = re.sub(r"<animateTransform[^>]*/>", "", svg)
    svg = svg.replace('opacity="0"', 'opacity="1"')
    return svg


for name, theme in (("preview_dark", B.DARK), ("preview_light", B.LIGHT)):
    svg = B.build(theme, cells)
    svg = strip(svg)
    with open(name + ".svg", "w", encoding="utf-8") as f:
        f.write(svg)
    print(name + ".svg written")
