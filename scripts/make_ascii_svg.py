from PIL import Image
import os

INPUT = "profile-prepped.png"
OUTPUT = "qazi-ascii.svg"
COLS = 100
ROWS = 53
RAMP = " .`:-=+*cs#%@@"
FILL_COLOR = "#c9d1d9"
BG_COLOR = "#0d1117"
FONT_SIZE = 8


def quantize(val):
    idx = int((val / 255) * (len(RAMP) - 1))
    return RAMP[min(idx, len(RAMP) - 1)]


def main():
    if not os.path.exists(INPUT):
        print(f"{INPUT} not found, skipping ASCII generation")
        return

    img = Image.open(INPUT).convert("L")
    w, h = img.size
    aspect = h / w
    target_cols = COLS
    target_rows = int(target_cols * aspect * 0.55)
    if target_rows > ROWS:
        target_rows = ROWS

    img_small = img.resize((target_cols, target_rows), Image.LANCZOS)
    pixels = list(img_small.getdata())
    chars = [quantize(p) for p in pixels]

    cell_w = FONT_SIZE * 0.6
    cell_h = FONT_SIZE * 1.15
    svg_w = target_cols * cell_w
    svg_h = target_rows * cell_h + 20

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">')
    lines.append(f'<rect width="100%" height="100%" fill="{BG_COLOR}"/>')
    lines.append(f'<g font-family="monospace" font-size="{FONT_SIZE}" fill="{FILL_COLOR}">')

    stagger_ms = 30

    for row in range(target_rows):
        start_y = row * cell_h + 10
        row_chars = chars[row * target_cols:(row + 1) * target_cols]
        line = "".join(row_chars)
        delay = row * stagger_ms
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        lines.append(f'<text x="0" y="{start_y}" xml:space="preserve">')
        lines.append(f'<animate attributeName="opacity" from="0" to="1" begin="{delay}ms" dur="500ms" fill="freeze"/>')
        lines.append(f'{escaped}')
        lines.append(f'</text>')

    lines.append("</g>")
    lines.append("</svg>")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {OUTPUT} ({target_cols} x {target_rows})")


if __name__ == "__main__":
    main()
