"""Build assets/skills.svg: one image with every skill icon in skillicons.dev style.

Icons skillicons.dev has are downloaded from it; the ones it lacks
(Assembly, Burp Suite, Oracle) are drawn here in the same tile style.
Edit ROWS, then run:  python3 assets/build_skills.py
"""
import re
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "skills.svg"

ROWS = [
    ["c", "cpp", "python", "java", "js", "php", "asm", "mysql", "postgres"],
    ["ubuntu", "debian", "linux", "vim", "vscode", "sublime", "docker", "github", "aws", "oracle", "burpsuite"],
]

TILE = '<rect width="256" height="256" rx="60" fill="#242938"/>'

CUSTOM = {
    # Burp Suite mark (Simple Icons, CC0), scaled into the tile
    "burpsuite": TILE + '<g transform="translate(48 48) scale(6.6667)" fill="#FF6633">'
    '<path d="M0 0v24h24V0Zm11.063 3.357h1.874v2.756L10.41 9.2h2.527v3.748h4.579l-4.578 5.592v2.104h-1.876v-2.758l2.528-3.086h-2.527V11.05h-4.58l4.58-5.592Z"/></g>',
    # Oracle: red rounded ring
    "oracle": TILE + '<rect x="40" y="86" width="176" height="84" rx="42" fill="none" stroke="#C74634" stroke-width="22"/>',
    # Assembly: plain mnemonic tile
    "asm": TILE + '<text x="128" y="150" text-anchor="middle" fill="#00FF9C" '
    'font-family="JetBrains Mono,Fira Code,Menlo,Consolas,monospace" font-size="74" font-weight="800">ASM</text>'
    '<text x="128" y="200" text-anchor="middle" fill="#8b949e" '
    'font-family="JetBrains Mono,Fira Code,Menlo,Consolas,monospace" font-size="30">x86 · ARM</text>',
}

SIZE = 48
PITCH = 56


def icon_body(name):
    if name in CUSTOM:
        return CUSTOM[name]
    url = f"https://skillicons.dev/icons?i={name}&theme=dark"
    req = urllib.request.Request(url, headers={"User-Agent": "readme-builder"})
    svg = urllib.request.urlopen(req, timeout=20).read().decode()
    inner = re.search(r"<g transform=\"translate\(0, 0\)\">(.*)</g>", svg, re.S)
    if not inner or len(svg) < 400:
        raise SystemExit(f"skillicons has no icon named {name!r}")
    return inner.group(1)


def main():
    width = max(len(r) for r in ROWS) * PITCH - (PITCH - SIZE)
    height = len(ROWS) * PITCH - (PITCH - SIZE)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
             f'width="{width}" height="{height}" viewBox="0 0 {width} {height}">']
    for r, row in enumerate(ROWS):
        offset = (width - (len(row) * PITCH - (PITCH - SIZE))) / 2
        for c, name in enumerate(row):
            x, y = offset + c * PITCH, r * PITCH
            body = icon_body(name)
            parts.append(f'<svg x="{x}" y="{y}" width="{SIZE}" height="{SIZE}" viewBox="0 0 256 256">'
                         f'<title>{name}</title>{body}</svg>')
    parts.append("</svg>")
    OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
    print(f"wrote assets/skills.svg ({width}x{height})")


if __name__ == "__main__":
    main()
