import os

OUTPUT = "info-card.svg"
STATIC = os.environ.get("STATIC", "0") == "1"

WIDTH = 490
HEIGHT = 380
BG = "#0d1117"
FG = "#c9d1d9"
ACCENT = "#00F7FF"
GREEN = "#26a641"
YELLOW = "#e3b341"
DIM = "#8b949e"

DATA = {
    "User": "Qazi Farhan Ahmad",
    "Role": "AI Web Developer + MERN",
    "College": "University of Peshawar",
    "Semester": "BS SE • 4th",
    "Stack": "React • Next • Node • TS",
    "Database": "MongoDB • Postgres • Redis",
    "AI Stack": "Groq • Gemini • OpenAI",
    "Focus": "AI-Powered Web Apps",
    "Location": "Peshawar, Pakistan",
    "Status": "Shipping production systems",
}


def anim(delay, dur="500ms"):
    if STATIC:
        return ""
    a = f'<animate attributeName="opacity" from="0" to="1" begin="{delay}ms" dur="{dur}" fill="freeze"/>'
    t = f'<animateTransform attributeName="transform" type="translate" from="0 -6" to="0 0" begin="{delay}ms" dur="{dur}" fill="freeze"/>'
    return a + t


def make_svg():
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">')
    lines.append(f'<rect width="100%" height="100%" fill="{BG}" rx="8"/>')

    y = 0
    stagger = 80

    # Title bar
    title_y = 32
    lines.append(f'<rect x="16" y="{y}" width="{WIDTH - 32}" height="28" rx="4" fill="#161b22"/>')
    lines.append(f'<circle cx="28" cy="14" r="5" fill="#ff5555"/>')
    lines.append(f'<circle cx="46" cy="14" r="5" fill="#f1fa8c"/>')
    lines.append(f'<circle cx="64" cy="14" r="5" fill="#50fa7b"/>')
    lines.append(f'<text x="82" y="20" font-family="monospace" font-size="11" fill="{DIM}">qazi@github -- ~ -- bash</text>')

    lines.append(f'<text x="16" y="{title_y + 30}" font-family="monospace" font-size="13" fill="{ACCENT}">')
    lines.append(anim(stagger))
    lines.append(f'<tspan font-weight="bold" fill="{YELLOW}">qazi@github</tspan>')
    lines.append(f'<tspan fill="{DIM}">:~$ </tspan>')
    lines.append(f'<tspan>whoami</tspan>')
    lines.append(f'</text>')

    lines.append(f'<text x="16" y="{title_y + 60}" font-family="monospace" font-size="13" fill="{FG}">')
    lines.append(anim(stagger + 50))
    lines.append(f'<tspan fill="{GREEN}">  > Qazi Farhan Ahmad</tspan>')
    lines.append(f'</text>')

    lines.append(f'<text x="16" y="{title_y + 80}" font-family="monospace" font-size="11" fill="{DIM}">')
    lines.append(anim(stagger + 50))
    lines.append(f'<tspan fill="{ACCENT}">  > Role: </tspan>')
    lines.append(f'<tspan>AI Web Developer | MERN Stack</tspan>')
    lines.append(f'</text>')

    items = list(DATA.items())
    for i, (key, val) in enumerate(items[2:], start=4):
        t = title_y + 20 + i * 22
        delay = stagger + i * 60
        lines.append(f'<text x="16" y="{t}" font-family="monospace" font-size="11">')
        lines.append(anim(delay))
        lines.append(f'<tspan fill="{ACCENT}">  > {key}: </tspan>')
        lines.append(f'<tspan fill="{FG}">{val}</tspan>')
        lines.append(f'</text>')

    # Blinking cursor
    cursor_y = title_y + 20 + (len(items) + 1) * 22 + 6
    lines.append(f'<rect x="16" y="{cursor_y}" width="8" height="14" rx="1" fill="{ACCENT}">')
    if not STATIC:
        lines.append(f'<animate attributeName="opacity" values="1;0;1" dur="1.2s" repeatCount="indefinite"/>')
    lines.append(f'</rect>')

    lines.append("</svg>")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    make_svg()
