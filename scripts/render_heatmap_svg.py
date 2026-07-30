import json
import os

DATA_FILE = "data/contributions.json"
OUTPUT = "contrib-heatmap.svg"

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
BG = "#0d1117"
FG = "#c9d1d9"
DIM = "#8b949e"
ACCENT = "#00F7FF"
GREEN = "#26a641"

CELL = 12
GAP = 2
LABEL_W = 30
HEADER_H = 40
FOOTER_H = 40
PAD = 20

MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
DAY_LABELS = ["", "Mon", "", "Wed", "", "Fri", ""]


def level(count):
    if count == 0:
        return 0
    if count <= 3:
        return 1
    if count <= 6:
        return 2
    if count <= 9:
        return 3
    if count <= 12:
        return 4
    return 5


def build_svg(days, total, streak, longest_streak, best_day):
    n = len(days)
    weeks = (n + 6) // 7
    cols = weeks * (CELL + GAP)

    W = cols + LABEL_W + PAD * 2
    H = 7 * (CELL + GAP) + HEADER_H + FOOTER_H + PAD * 2

    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">')
    lines.append(f'<rect width="100%" height="100%" fill="{BG}"/>')
    lines.append("<style>")
    lines.append("@keyframes reveal{0%{opacity:0;transform:scale(0.3)}100%{opacity:1;transform:scale(1)}}")
    lines.append("</style>")

    x_off = LABEL_W + PAD
    y_off = HEADER_H + PAD

    # Day labels
    for dy, label in enumerate(DAY_LABELS):
        if label:
            y = y_off + dy * (CELL + GAP) + CELL // 2 + 4
            lines.append(f'<text x="{PAD + 4}" y="{y}" font-family="monospace" font-size="9" fill="{DIM}">{label}</text>')

    # Month labels
    prev_month = ""
    month_col_x = {}
    for i, d in enumerate(days):
        month = d["date"][5:7]
        if month != prev_month:
            col = i // 7
            mx = x_off + col * (CELL + GAP)
            month_label = MONTH_LABELS[int(month) - 1]
            if month_label not in month_col_x:
                month_col_x[month_label] = mx
            prev_month = month

    for ml, mx in month_col_x.items():
        lines.append(f'<text x="{mx}" y="{HEADER_H + PAD - 8}" font-family="monospace" font-size="9" fill="{DIM}">{ml}</text>')

    # Cells
    for i, d in enumerate(days):
        week = i // 7
        day = i % 7
        x = x_off + week * (CELL + GAP)
        y = y_off + day * (CELL + GAP)
        lv = level(d["count"])
        color = PALETTE[lv]
        delay = (week * 3 + day * 2) * 15
        lines.append(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="3" fill="{color}" '
                     f'style="animation:reveal 0.4s ease {delay}ms both"/>'
                     f'<title>{d["date"]}: {d["count"]} contributions</title>')

    # Legend
    leg_x = x_off + cols - 120
    leg_y = y_off + 7 * (CELL + GAP) + 12
    lines.append(f'<text x="{leg_x}" y="{leg_y}" font-family="monospace" font-size="9" fill="{DIM}">Less</text>')
    for lv in range(5):
        lx = leg_x + 32 + lv * (CELL + 3)
        lines.append(f'<rect x="{lx}" y="{leg_y - 6}" width="{CELL}" height="{CELL}" rx="2" fill="{PALETTE[lv + 1]}"/>')
    lines.append(f'<text x="{leg_x + 32 + 5 * (CELL + 3) + 4}" y="{leg_y}" font-family="monospace" font-size="9" fill="{DIM}">More</text>')

    # Stats footer
    fty = y_off + 7 * (CELL + GAP) + 40
    lines.append(f'<text x="{PAD}" y="{fty}" font-family="monospace" font-size="12" fill="{FG}" font-weight="bold">')
    lines.append(f'<tspan fill="{ACCENT}">{total}</tspan>')
    lines.append(f'<tspan fill="{DIM}"> contributions in the last year</tspan>')
    lines.append(f'</text>')
    lines.append(f'<text x="{PAD}" y="{fty + 18}" font-family="monospace" font-size="10" fill="{DIM}">')
    lines.append(f'<tspan fill="{GREEN}">{streak}</tspan> day streak &middot; ')
    lines.append(f'<tspan fill="{GREEN}">{longest_streak}</tspan> longest &middot; ')
    lines.append(f'Best day: {best_day.get("date", "")} ({best_day.get("count", 0)})')
    lines.append(f'</text>')

    lines.append("</svg>")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {OUTPUT}")


def main():
    if not os.path.exists(DATA_FILE):
        print(f"{DATA_FILE} not found, skipping heatmap render")
        return
    with open(DATA_FILE) as f:
        data = json.load(f)
    build_svg(
        days=data["days"],
        total=data["total"],
        streak=data["streak"],
        longest_streak=data["longest_streak"],
        best_day=data["best_day"],
    )


if __name__ == "__main__":
    main()
