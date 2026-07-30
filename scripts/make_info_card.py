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


def make_svg():
    lines = []
    lines.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {HEIGHT}" width="{WIDTH}" height="{HEIGHT}">')
    lines.append(f'<rect width="100%" height="100%" fill="{BG}" rx="8"/>')
    lines.append("<style>")
    lines.append("@keyframes slideIn{0%{opacity:0;transform:translateY(-6px)}100%{opacity:1;transform:translateY(0)}}")
    lines.append("@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}")
    lines.append("</style>")

    y = 0
    stagger = 80

    # Title bar
    title_y = 32
    lines.append(f'<rect x="16" y="{y}" width="{WIDTH - 32}" height="28" rx="4" fill="#161b22"/>')
    lines.append(f'<circle cx="28" cy="14" r="5" fill="#ff5555"/>')
    lines.append(f'<circle cx="46" cy="14" r="5" fill="#f1fa8c"/>')
    lines.append(f'<circle cx="64" cy="14" r="5" fill="#50fa7b"/>')
    lines.append(f'<text x="82" y="20" font-family="monospace" font-size="11" fill="{DIM}">qazi@github -- ~ -- bash</text>')
    an = f"animation:slideIn 0.5s ease {stagger}ms both"
    lines.append(f'<text x="16" y="{title_y + 30}" font-family="monospace" font-size="13" fill="{ACCENT}" style="{an}">')
    lines.append(f'<tspan font-weight="bold" fill="{YELLOW}">qazi@github</tspan>')
    lines.append(f'<tspan fill="{DIM}">:~$ </tspan>')
    lines.append(f'<tspan>whoami</tspan>')
    lines.append(f'</text>')

    an = f"animation:slideIn 0.5s ease {(stagger + 40)}ms both"
    lines.append(f'<text x="16" y="{title_y + 60}" font-family="monospace" font-size="13" fill="{FG}" style="{an}">')
    lines.append(f'<tspan fill="{GREEN}">  > Qazi Farhan Ahmad</tspan>')
    lines.append(f'</text>')

    an = f"animation:slideIn 0.5s ease {(stagger + 40)}ms both"
    lines.append(f'<text x="16" y="{title_y + 80}" font-family="monospace" font-size="11" fill="{DIM}" style="{an}">')
    lines.append(f'<tspan fill="{ACCENT}">  > Role: </tspan>')
    lines.append(f'<tspan>AI Web Developer | MERN Stack</tspan>')
    lines.append(f'</text>')

    items = list(DATA.items())
    for i, (key, val) in enumerate(items[2:], start=4):
        t = title_y + 20 + i * 22
        delay = stagger + i * 60
        an = f"animation:slideIn 0.5s ease {delay}ms both"
        lines.append(f'<text x="16" y="{t}" font-family="monospace" font-size="11" style="{an}">')
        lines.append(f'<tspan fill="{ACCENT}">  > {key}: </tspan>')
        lines.append(f'<tspan fill="{FG}">{val}</tspan>')
        lines.append(f'</text>')

    # Blinking cursor
    cursor_y = title_y + 20 + (len(items)) * 22 + 10
    lines.append(f'<rect x="16" y="{cursor_y}" width="8" height="14" rx="1" fill="{ACCENT}" style="animation:blink 1.2s step-end infinite"/>')

    lines.append("</svg>")

    with open(OUTPUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    make_svg()
