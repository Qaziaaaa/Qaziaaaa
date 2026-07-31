import math
import os
import random

import numpy as np
import scipy.ndimage as ndi
from PIL import Image, ImageOps, ImageEnhance, ImageFilter

PHOTO = "profile.jpg"

WINDOW_W = 1180
WINDOW_H = 610
TITLE_H = 40

PORT_X = 30
PORT_Y = 85
CS = 1.4
GRID_W = 300
GRID_H = 340
PORT_W = GRID_W * CS
PORT_H = GRID_H * CS

INFO_X = 474
INFO_RIGHT = 1140

FONT = "'JetBrains Mono','Fira Code',monospace"

N_INTRO = 60
N_BANDS = 60
N_TRAVELERS = 900
LOOP_BEGIN = 3.2
LOOP_DUR = 14.2
KT = [0, 0.2113, 0.3028, 0.4437, 0.5352, 0.6761, 0.7676, 0.9085, 1]

ACOLS = 77
AROWS = 52
FONT_SIZE = 9.0
CELL_W = 5.4
CELL_H = 9.0
CHAR_RAMP = " .:-=+*#%@"

DARK = {
    "bg": "#1a1b26", "panel": "#16161e", "border": "#24283b",
    "chrome": "#00F7FF", "chrome_dim": "#3b4261", "accent": "#9ece6a",
    "dots": "#bb9af7", "traveler": "#c0caf5",
    "text": "#a9b1d6", "dim": "#565f89", "leader": "#3b4261",
    "red": "#f7768e", "green": "#9ece6a", "pane_dot": "#414868",
}

LIGHT = {
    "bg": "#e1e2e7", "panel": "#ffffff", "border": "#c8ccdf",
    "chrome": "#3760bf", "chrome_dim": "#9aa5ce", "accent": "#0b8494",
    "dots": "#7C3AED", "traveler": "#6D28D9",
    "text": "#343b58", "dim": "#5a6177", "leader": "#c0c4da",
    "red": "#dc2626", "green": "#0b8494", "pane_dot": "#c8ccdf",
}

INFO_ROWS = [
    ("Subject", "Qazi Farhan Ahmad"),
    ("Role", "AI Web Developer + MERN"),
    ("Origin", "Peshawar, Pakistan"),
    ("Education", "BS SE - Univ. of Peshawar"),
    ("Status", "Building + Learning + Shipping"),
    ("ToolChain", "VS Code, Git, Docker, Vercel"),
    ("Core.Lang", "TypeScript, JavaScript, Python"),
    ("Core.Frontend", "React, Next.js, Vite, Tailwind"),
    ("Core.Backend", "Node.js, Express.js"),
    ("Core.Database", "MongoDB, PostgreSQL, Redis"),
    ("Core.Infra", "Vercel, Docker, Firebase"),
    ("Grid.Mail", "qazithekingston@gmail.com"),
    ("Grid.Portfolio", "qaziahmad.vercel.app"),
    ("Grid.LinkedIn", "linkedin.com/in/qazi-farhan-ahmad"),
    ("Grid.GitHub", "github.com/Qaziaaaa"),
    ("Grid.Social", "WhatsApp +92 314 1935787"),
]

PORT_CX = PORT_X + PORT_W / 2
PORT_CY = PORT_Y + PORT_H / 2


# ---------------------------------------------------------------- photo

def load_and_crop():
    img = Image.open(PHOTO)
    img = ImageOps.exif_transpose(img).convert("RGB")
    w, h = img.size
    target = GRID_W / GRID_H
    if w / h > target:
        new_w = int(h * target)
        x0 = (w - new_w) // 2
        img = img.crop((x0, 0, x0 + new_w, h))
    else:
        new_h = int(w / target)
        y0 = int((h - new_h) * 0.35)
        img = img.crop((0, y0, w, y0 + new_h))
    return img.resize((GRID_W, GRID_H), Image.LANCZOS)


def preprocess(img):
    img = ImageOps.autocontrast(img, cutoff=1)
    img = ImageEnhance.Contrast(img).enhance(1.3)
    img = img.filter(ImageFilter.UnsharpMask(radius=3, percent=140))
    return np.asarray(img.convert("L"), dtype=np.float64)


def segment_mask(img_rgb):
    rgb = np.asarray(img_rgb, dtype=np.float64)
    border = np.concatenate([rgb[0, :], rgb[-1, :], rgb[:, 0], rgb[:, -1]], axis=0)
    bg = np.median(border, axis=0)
    dist = np.linalg.norm(rgb - bg, axis=2)
    mask = dist > 45
    mask = ndi.binary_closing(mask, structure=np.ones((3, 3)), iterations=2)
    mask = ndi.binary_fill_holes(mask)
    lbl, n = ndi.label(mask)
    if n > 0:
        sizes = ndi.sum(mask, lbl, range(1, n + 1))
        mask = lbl == (int(np.argmax(sizes)) + 1)
    return mask


def ascii_gray(img):
    g = ImageOps.autocontrast(img, cutoff=1)
    g = ImageEnhance.Contrast(g).enhance(1.15)
    return np.asarray(g.convert("L"), dtype=np.float64)


def ascii_cells(gray, mask):
    m_full = ndi.binary_erosion(mask, iterations=1)
    g = Image.fromarray(gray.astype(np.uint8)).resize((ACOLS, AROWS), Image.BILINEAR)
    m = Image.fromarray((m_full * 255).astype(np.uint8)).resize((ACOLS, AROWS), Image.NEAREST)
    g = np.asarray(g, dtype=np.float64)
    m = np.asarray(m) > 128
    vals = g[m]
    lo, hi = np.percentile(vals, 2), np.percentile(vals, 98)
    span = max(hi - lo, 1e-6)
    cells = []
    for r in range(AROWS):
        for c in range(ACOLS):
            if not m[r, c]:
                continue
            t = (g[r, c] - lo) / span
            t = float(np.clip(t, 0, 1))
            cells.append((r, c, CHAR_RAMP[int((1 - t) * (len(CHAR_RAMP) - 1))]))
    return cells


# ---------------------------------------------------------------- logos

def _sample_segment(pts, cx, cy, s, step=1.4):
    out = []
    for (x0, y0, x1, y1) in pts:
        ax, ay = cx + x0 * s, cy + y0 * s
        bx, by = cx + x1 * s, cy + y1 * s
        d = math.hypot(bx - ax, by - ay)
        n = max(1, int(d / step))
        for i in range(n + 1):
            t = i / n
            out.append((ax + (bx - ax) * t, ay + (by - ay) * t))
    return out


def logo_react(s=62):
    pts = []
    for a in range(0, 360, 45):
        pts.append((PORT_CX + 4 * math.cos(math.radians(a)),
                    PORT_CY + 4 * math.sin(math.radians(a))))
    rx, ry = s, s * 0.28
    for rot in (0, 60, 120):
        for a in range(0, 360, 3):
            x = rx * math.cos(math.radians(a))
            y = ry * math.sin(math.radians(a))
            xr = x * math.cos(math.radians(rot)) - y * math.sin(math.radians(rot))
            yr = x * math.sin(math.radians(rot)) + y * math.cos(math.radians(rot))
            pts.append((PORT_CX + xr, PORT_CY + yr))
    return pts


def logo_terminal():
    segs = [
        (-46, -36, -12, 0), (-46, 36, -12, 0),
        (46, -36, 12, 0), (46, 36, 12, 0),
        (-8, -36, 8, 36),
    ]
    return _sample_segment(segs, PORT_CX, PORT_CY, 1.0)


def logo_bolt(s=1.05):
    poly = [(-12, -48), (14, -6), (2, -6), (12, 48), (-14, 6), (-2, 6)]
    segs = []
    for i in range(len(poly)):
        x0, y0 = poly[i]
        x1, y1 = poly[(i + 1) % len(poly)]
        segs.append((x0, y0, x1, y1))
    return _sample_segment(segs, PORT_CX, PORT_CY, s, step=1.6)


def sorted_pts(pts):
    return sorted(pts, key=lambda p: math.atan2(p[1] - PORT_CY, p[0] - PORT_CX))


# ---------------------------------------------------------------- svg

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def header(theme):
    return [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WINDOW_W}" height="{WINDOW_H}" '
        f'viewBox="0 0 {WINDOW_W} {WINDOW_H}">',
        f'<rect width="{WINDOW_W}" height="{WINDOW_H}" fill="{theme["bg"]}"/>',
    ]


def window_chrome(theme):
    l = []
    l.append(f'<rect x="10" y="6" width="{WINDOW_W - 20}" height="{WINDOW_H - 12}" rx="12" '
             f'fill="none" stroke="{theme["border"]}" stroke-width="2"/>')
    l.append(f'<rect x="10" y="6" width="{WINDOW_W - 20}" height="{TITLE_H}" rx="12" fill="{theme["panel"]}"/>')
    l.append(f'<rect x="10" y="{TITLE_H - 2}" width="{WINDOW_W - 20}" height="4" fill="{theme["panel"]}"/>')
    for i, c in enumerate(("#FF5F56", "#FFBD2E", "#27C93F")):
        l.append(f'<circle cx="{26 + i * 22}" cy="26" r="6" fill="{c}" opacity="0.9"/>')
    l.append(f'<text x="590" y="29" font-family="{FONT}" font-size="14" fill="{theme["dim"]}" '
             f'text-anchor="middle">{esc("profile.sh --live")}</text>')
    l.append(f'<text x="{WINDOW_W - 30}" y="29" font-family="{FONT}" font-size="13" fill="{theme["chrome"]}" '
             f'text-anchor="end">qazi@github</text>')
    return l


def portrait_frame(theme):
    l = []
    l.append(f'<text x="28" y="70" font-family="{FONT}" font-size="13" fill="{theme["chrome_dim"]}">'
             f'<tspan fill="{theme["chrome"]}">VISUAL</tspan>.MAP</text>')
    return l


def info_panel(theme):
    l = []
    l.append(f'<text x="{INFO_X}" y="68" font-family="{FONT}" font-size="13" fill="{theme["chrome_dim"]}">'
             f'<tspan fill="{theme["chrome"]}">SYSTEM</tspan>.INFO</text>')
    # pulsing LIVE badge
    l.append(f'<g>')
    l.append(f'<rect x="1070" y="56" width="66" height="24" rx="12" fill="{theme["red"]}" opacity="0.15"/>')
    l.append(f'<circle cx="1082" cy="68" r="4" fill="{theme["red"]}">'
             f'<animate attributeName="opacity" values="1;0.25;1" dur="1.4s" repeatCount="indefinite"/>'
             f'</circle>')
    l.append(f'<text x="1092" y="72" font-family="{FONT}" font-size="12" font-weight="bold" '
             f'fill="{theme["red"]}">LIVE</text>')
    l.append(f'</g>')

    y = 116
    spacing = 23
    for label, value in INFO_ROWS:
        lw = len(label) * 8.4
        vw = len(value) * 8.4
        ls = INFO_X + lw + 8
        le = INFO_RIGHT - vw - 8
        if le - ls > 8:
            l.append(f'<path d="M {ls} {y} H {le}" stroke="{theme["leader"]}" stroke-width="2" '
                     f'stroke-dasharray="1 4" stroke-linecap="round"/>')
        l.append(f'<text x="{INFO_X}" y="{y}" font-family="{FONT}" font-size="14" '
                 f'fill="{theme["dim"]}" textLength="{lw}" lengthAdjust="spacingAndGlyphs">{esc(label)}</text>')
        l.append(f'<text x="{INFO_RIGHT}" y="{y}" font-family="{FONT}" font-size="14" '
                 f'fill="{theme["text"]}" text-anchor="end" textLength="{vw}" '
                 f'lengthAdjust="spacingAndGlyphs">{esc(value)}</text>')
        y += spacing

    l.append(f'<rect x="{INFO_X}" y="558" width="{INFO_RIGHT - INFO_X}" height="36" rx="6" '
             f'fill="{theme["panel"]}" stroke="{theme["border"]}" stroke-width="1.5"/>')
    l.append(f'<circle cx="{INFO_X + 14}" cy="576" r="4" fill="{theme["green"]}"/>')
    l.append(f'<text x="{INFO_X + 26}" y="580" font-family="{FONT}" font-size="13" '
             f'fill="{theme["dim"]}">ready · {esc("qazi@github:~/profile")}</text>')
    l.append(f'<rect x="974" y="566" width="150" height="20" rx="10" fill="{theme["accent"]}" opacity="0.15"/>')
    l.append(f'<text x="1049" y="581" font-family="{FONT}" font-size="13" font-weight="bold" '
             f'text-anchor="middle" fill="{theme["accent"]}">@Qaziaaaa</text>')
    return l


def portrait_layer(theme, cells):
    grid = [[" "] * ACOLS for _ in range(AROWS)]
    for (r, c, ch) in cells:
        grid[r][c] = ch

    out = []
    out.append(f'<g font-family="monospace" font-size="{FONT_SIZE}" fill="{theme["dots"]}">')
    for r in range(AROWS):
        line = "".join(grid[r]).rstrip()
        if not line.strip():
            continue
        out.append(f'<text x="{PORT_X:.1f}" y="{PORT_Y + r * CELL_H + CELL_H * 0.8:.1f}" '
                   f'textLength="{PORT_W:.1f}" xml:space="preserve">{esc(line)}</text>')
    out.append(f'</g>')
    return out


def traveler_layer(theme):
    l1 = sorted_pts(logo_react())
    l2 = sorted_pts(logo_terminal())
    l3 = sorted_pts(logo_bolt())
    kt = ";".join(f"{t:.4f}" for t in KT)
    out = []
    out.append(f'<g opacity="0">')
    out.append(f'<animate attributeName="opacity" values="0;0;1;1;1;1;1;1;0" keyTimes="{kt}" '
               f'begin="{LOOP_BEGIN}s" dur="{LOOP_DUR}s" repeatCount="indefinite"/>')
    for i in range(N_TRAVELERS):
        p1 = l1[i % len(l1)]
        p2 = l2[i % len(l2)]
        p3 = l3[i % len(l3)]
        vx = ";".join(f"{v:.1f}" for v in [p1[0], p1[0], p1[0], p2[0], p2[0], p3[0], p3[0], p1[0], p1[0]])
        vy = ";".join(f"{v:.1f}" for v in [p1[1], p1[1], p1[1], p2[1], p2[1], p3[1], p3[1], p1[1], p1[1]])
        out.append(f'<circle r="1.5" fill="{theme["traveler"]}">')
        out.append(f'<animate attributeName="cx" values="{vx}" keyTimes="{kt}" '
                   f'begin="{LOOP_BEGIN}s" dur="{LOOP_DUR}s" repeatCount="indefinite"/>')
        out.append(f'<animate attributeName="cy" values="{vy}" keyTimes="{kt}" '
                   f'begin="{LOOP_BEGIN}s" dur="{LOOP_DUR}s" repeatCount="indefinite"/>')
        out.append(f'</circle>')
    out.append(f'</g>')
    return out


def build(theme, cells):
    parts = []
    parts += header(theme)
    parts += window_chrome(theme)
    parts += portrait_frame(theme)
    parts += info_panel(theme)
    parts += portrait_layer(theme, cells)
    parts.append("</svg>")
    return "\n".join(parts)


def main():
    img = load_and_crop()
    gray = ascii_gray(img)
    mask = segment_mask(img)
    cells = ascii_cells(gray, mask)

    with open("dark.svg", "w", encoding="utf-8") as f:
        f.write(build(DARK, cells))
    print("dark.svg written")

    with open("light.svg", "w", encoding="utf-8") as f:
        f.write(build(LIGHT, cells))
    print("light.svg written")


if __name__ == "__main__":
    main()
