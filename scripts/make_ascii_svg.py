from PIL import Image
import os

INPUT = "profile-prepped.png"
OUTPUT = "qazi-ascii.svg"
COLS = 100
ROWS = 53
RAMP = " .`:-=+*cs#%@@"
FILL_COLOR = "#c9d1d9"
BG_COLOR = "#0d1117"
CURSOR_COLOR = "#00F7FF"
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

    stagger_ms = 40
    dur_ms = 250
    cursor_w = 6
    cursor_h = FONT_SIZE + 3

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {svg_w} {svg_h}" width="{svg_w}" height="{svg_h}">')
    lines.append(f'<rect width="100%" height="100%" fill="{BG_COLOR}"/>')
    lines.append('<defs>')

    for row in range(target_rows):
        delay = row * stagger_ms
        lines.append(f'<clipPath id="cp{row}">')
        lines.append(f'<rect x="0" y="0" width="0" height="{svg_h}">')
        lines.append(f'<animate attributeName="width" from="0" to="{svg_w}" begin="{delay}ms" dur="{dur_ms}ms" fill="freeze" calcMode="linear"/>')
        lines.append(f'</rect>')
        lines.append(f'</clipPath>')

    lines.append('</defs>')
    lines.append(f'<g font-family="monospace" font-size="{FONT_SIZE}" fill="{FILL_COLOR}">')

    for row in range(target_rows):
        start_y = row * cell_h + 10
        row_chars = chars[row * target_cols:(row + 1) * target_cols]
        line = "".join(row_chars)
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        lines.append(f'<text x="0" y="{start_y}" clip-path="url(#cp{row})" xml:space="preserve">{escaped}</text>')

    lines.append('</g>')

    for row in range(target_rows):
        row_chars = chars[row * target_cols:(row + 1) * target_cols]
        if all(c == " " for c in row_chars):
            continue
        start_y = row * cell_h + 10
        delay = row * stagger_ms
        lines.append(f'<rect x="0" y="{start_y - FONT_SIZE}" width="{cursor_w}" height="{cursor_h}" fill="{CURSOR_COLOR}">')
        lines.append(f'<animateTransform attributeName="transform" type="translate" from="0 0" to="{svg_w} 0" begin="{delay}ms" dur="{dur_ms}ms" fill="freeze" calcMode="linear"/>')
        lines.append(f'<animate attributeName="opacity" values="1;1;0" keyTimes="0;0.9;1" begin="{delay}ms" dur="{dur_ms + 80}ms" fill="freeze"/>')
        lines.append(f'</rect>')

    lines.append('</svg>')

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {OUTPUT} ({target_cols} x {target_rows}, {dur_ms}ms/row, {stagger_ms}ms stagger)")


if __name__ == "__main__":
    main()
