"""Render the README terminal blocks as always-dark SVG images.

Edit the BLOCKS below, then run:  python3 assets/build_terminals.py
Each block becomes assets/<name>.svg.
"""
from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).resolve().parent

# palette
BG = "#000000"
BAR = "#2b2b2b"  # Ubuntu (Yaru dark) header bar
ORANGE = "#e95420"  # Ubuntu orange
U_GREEN = "#8ae234"  # Ubuntu terminal prompt green
U_BLUE = "#729fcf"  # Ubuntu terminal prompt blue
BORDER = "#0f3d24"
FG = "#c9d1d9"
DIM = "#5c6370"
GREEN = "#00ff9c"
GREEN2 = "#3fb950"
BLUE = "#58a6ff"
CYAN = "#39c5cf"
YELLOW = "#e3b341"
RED = "#ff5f56"
PURPLE = "#bc8cff"

FONT = 14
LINE_H = 21
CHAR_W = FONT * 0.6
PAD_X = 22
COLS = 92  # every image gets the same width so fonts scale identically
WIDTH = round(PAD_X * 2 + COLS * CHAR_W)
TITLE_H = 36


def prompt(cmd):
    return [
        [("J0hnwood@ubuntu", U_GREEN), (":", FG), ("~", U_BLUE), ("$ ", FG), (cmd, FG)],
        [],
    ]


BLOCKS = {
    "boot": ("J0hnwood@ubuntu: ~ — journalctl -b", [
        [("[  ", FG), ("OK", GREEN), ("  ] ", FG), ("Loading kernel modules ......................... ", FG), ("done", GREEN)],
        [("[  ", FG), ("OK", GREEN), ("  ] ", FG), ("Mounting /dev/brain ............................ ", FG), ("done", GREEN)],
        [("[  ", FG), ("OK", GREEN), ("  ] ", FG), ("Starting caffeine.service ...................... ", FG), ("done", GREEN)],
        [("[  ", FG), ("OK", GREEN), ("  ] ", FG), ("Starting exploit-dev.service ................... ", FG), ("done", GREEN)],
        [("[  ", FG), ("OK", GREEN), ("  ] ", FG), ("Starting reverse-engineering.service ........... ", FG), ("done", GREEN)],
        [("[ ", FG), ("WARN", YELLOW), (" ] ", FG), ("sleep.service failed to start ", FG), ("(dependency: deadline)", DIM)],
        [("[  ", FG), ("OK", GREEN), ("  ] ", FG), ("Reached target: ", FG), ("J0hnwood online", GREEN)],
    ]),
    "about": ("J0hnwood@ubuntu: ~", prompt("cat about_me.txt") + [
        [("[*] ", BLUE), ("Studying cybersecurity, step by step", FG)],
        [("[*] ", BLUE), ("Focus  : ", CYAN), ("web exploitation · system internals · reverse engineering", FG)],
        [("[*] ", BLUE), ("Goal   : ", CYAN), ("build a solid foundation in offensive security & technical analysis", FG)],
        [("[*] ", BLUE), ("Also   : ", CYAN), ("Python automation, data collection & analysis", FG)],
        [("[*] ", BLUE), ("Into   : ", CYAN), ("intelligence & cyber-threat research", FG)],
    ]),
    "ps": ("J0hnwood@ubuntu: ~", prompt("ps aux | grep J0hnwood") + [
        [("USER      PID   %CPU  STAT  COMMAND", DIM)],
        [("J0hnwood  ", GREEN2), ("1337  42.0  ", FG), ("R+    ", GREEN), ("./c_cpp --memory --pointers --for-reversing", FG)],
        [("J0hnwood  ", GREEN2), ("1338  27.5  ", FG), ("R     ", GREEN), ("./python --automation --scraping --data-analysis", FG)],
        [("J0hnwood  ", GREEN2), ("1339  14.3  ", FG), ("S     ", CYAN), ("./web --http --auth --sqli --xss", FG)],
        [("J0hnwood  ", GREEN2), ("1340   9.8  ", FG), ("S     ", CYAN), ("./asm --x86 --arm --read-disassembly", FG)],
        [("J0hnwood  ", GREEN2), ("1341   6.4  ", FG), ("S     ", CYAN), ("./linux --internals --syscalls --elf", FG)],
        [("J0hnwood  ", GREEN2), ("1342   0.1  ", FG), ("Z     ", RED), ("./sleep   ", FG), ("# zombie process, rarely scheduled", DIM)],
    ]),
    "nmap": ("J0hnwood@ubuntu: ~", prompt("nmap -sV J0hnwood") + [
        [("Starting Nmap 7.95 ( https://nmap.org )", DIM)],
        [("Nmap scan report for ", FG), ("J0hnwood", GREEN), (" (127.0.0.1)", FG)],
        [("Host is ", FG), ("up", GREEN), (" (0.0013s latency).", FG)],
        [],
        [("PORT       STATE     SERVICE     VERSION", DIM)],
        [("22/tcp     ", FG), ("open      ", GREEN), ("linux       ", CYAN), ("Ubuntu 24.04 LTS (KDE) daily driver", FG)],
        [("80/tcp     ", FG), ("open      ", GREEN), ("web-hack    ", CYAN), ("Burp Suite · SQLi · XSS · SSRF · auth", FG)],
        [("443/tcp    ", FG), ("open      ", GREEN), ("python      ", CYAN), ("automation · scraping · data analysis", FG)],
        [("1337/tcp   ", FG), ("open      ", GREEN), ("pwn         ", CYAN), ("C/C++ · stack · ROP · heap (in progress)", FG)],
        [("3306/tcp   ", FG), ("open      ", GREEN), ("database    ", CYAN), ("MySQL · PostgreSQL", FG)],
        [("31337/tcp  ", FG), ("open      ", GREEN), ("reversing   ", CYAN), ("x86 / ARM assembly · IDA · Ghidra", FG)],
        [("8080/tcp   ", FG), ("filtered  ", YELLOW), ("sleep       ", CYAN), ("no response", DIM)],
        [],
        [("Nmap done: 1 IP address (1 host up) scanned in ", FG), ("13.37", GREEN), (" seconds", FG)],
    ]),
    "goals": ("J0hnwood@ubuntu: ~", prompt("cat goals.md") + [
        [("# ── [ PWN ] ", PURPLE), ("─" * 38, DIM)],
        [("[ ] ", RED), ("Bypass NX · ASLR · PIE · Canary and chain full ROP exploits", FG)],
        [("[ ] ", RED), ("glibc heap exploitation : tcache · fastbin · unsorted bin attacks", FG)],
        [("[ ] ", RED), ("Format string → arbitrary read / write → shell", FG)],
        [("[ ] ", RED), ("Linux kernel exploitation basics (UAF · race condition · ret2usr)", FG)],
        [],
        [("# ── [ WEB ] ", PURPLE), ("─" * 38, DIM)],
        [("[ ] ", RED), ("Chain bugs : SSRF → internal RCE, SSTI, insecure deserialization", FG)],
        [("[ ] ", RED), ("Break auth : JWT · OAuth · session logic flaws", FG)],
        [("[ ] ", RED), ("Prototype pollution & race conditions in modern web apps", FG)],
        [("[ ] ", RED), ("Submit valid reports to a real bug bounty program", FG)],
        [],
        [("# ── [ REVERSING ] ", PURPLE), ("─" * 32, DIM)],
        [("[ ] ", RED), ("Unpack packed binaries & defeat anti-debugging tricks", FG)],
        [("[ ] ", RED), ("Reverse Windows PE and Android apps (Frida hooking)", FG)],
        [("[ ] ", RED), ("Reproduce a public CVE from patch diff (1-day analysis)", FG)],
        [("[ ] ", RED), ("Fuzz a real target with AFL++ and triage the crashes", FG)],
        [],
        [("# ── [ MILESTONES ] ", PURPLE), ("─" * 31, DIM)],
        [("[ ] ", RED), ("Rank in the top tier of domestic CTFs with a team", FG)],
        [("[ ] ", RED), ("Earn a CVE of my own", FG)],
        [("[ ] ", RED), ("Publish deep technical write-ups for every challenge solved", FG)],
    ]),
    "closed": ("J0hnwood@ubuntu: ~", [
        [("[ connection closed by foreign host ]", DIM)],
    ]),
}


def window_buttons():
    """Ubuntu GNOME-style minimize / maximize / close on the right of the header bar."""
    cy, r, gap = TITLE_H / 2, 9, 26
    x3 = WIDTH - 22
    x2, x1 = x3 - gap, x3 - 2 * gap
    g = "#d0d0d0"
    return (
        f'<circle cx="{x1}" cy="{cy}" r="{r}" fill="#454545"/>'
        f'<line x1="{x1 - 4}" y1="{cy + 3}" x2="{x1 + 4}" y2="{cy + 3}" stroke="{g}" stroke-width="1.6"/>'
        f'<circle cx="{x2}" cy="{cy}" r="{r}" fill="#454545"/>'
        f'<rect x="{x2 - 4}" y="{cy - 4}" width="8" height="8" fill="none" stroke="{g}" stroke-width="1.4"/>'
        f'<circle cx="{x3}" cy="{cy}" r="{r}" fill="{ORANGE}"/>'
        f'<path d="M{x3 - 3.5} {cy - 3.5} L{x3 + 3.5} {cy + 3.5} M{x3 + 3.5} {cy - 3.5} L{x3 - 3.5} {cy + 3.5}" stroke="#fff" stroke-width="1.6"/>'
    )


def render(title, lines):
    body_h = PAD_X + len(lines) * LINE_H + PAD_X // 2
    height = TITLE_H + body_h
    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">',
        "<style>text{font-family:'JetBrains Mono','Fira Code',SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace;"
        f"font-size:{FONT}px;white-space:pre}}"
        "@keyframes b{50%{opacity:0}}.cur{animation:b 1s steps(1) infinite}</style>",
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>',
        f'<path d="M0.5 {TITLE_H} V10.5 a10 10 0 0 1 10 -10 H{WIDTH - 10.5} a10 10 0 0 1 10 10 V{TITLE_H} Z" fill="{BAR}"/>',
        f'<line x1="0.5" y1="{TITLE_H}" x2="{WIDTH - 0.5}" y2="{TITLE_H}" stroke="{BORDER}"/>',
        window_buttons(),
        f'<text x="{WIDTH / 2}" y="22" text-anchor="middle" fill="#cfcfcf" style="font-size:12px;font-weight:bold">{escape(title)}</text>',
    ]
    y = TITLE_H + PAD_X + 4
    for i, line in enumerate(lines):
        spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in line)
        if i == len(lines) - 1:
            # blinking block cursor, inline so it never overlaps whatever font the viewer has
            spans += f'<tspan class="cur" fill="{GREEN}"> █</tspan>'
        if spans:
            out.append(f'<text x="{PAD_X}" y="{y}" xml:space="preserve">{spans}</text>')
        y += LINE_H
    out.append("</svg>")
    return "\n".join(out) + "\n"


def render_banner():
    """Header: an Ubuntu terminal that prints the name in big glitchy neon."""
    height = 230
    cx = WIDTH / 2
    name_y = 162
    big = 'font-size:78px;font-weight:800;letter-spacing:4px'
    return "\n".join([
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="{height}" viewBox="0 0 {WIDTH} {height}">',
        "<defs>"
        '<filter id="glow" x="-20%" y="-50%" width="140%" height="200%">'
        '<feGaussianBlur stdDeviation="6" result="b"/>'
        '<feMerge><feMergeNode in="b"/><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
        '<pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">'
        '<rect width="4" height="1" fill="#ffffff" opacity="0.045"/></pattern>'
        '<radialGradient id="vig" cx="50%" cy="55%" r="65%">'
        '<stop offset="0%" stop-color="#00ff9c" stop-opacity="0.10"/>'
        '<stop offset="100%" stop-color="#000" stop-opacity="0"/></radialGradient>'
        "</defs>",
        "<style>text{font-family:'JetBrains Mono','Fira Code',SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace;"
        f"font-size:{FONT}px;white-space:pre}}"
        "@keyframes b{50%{opacity:0}}.cur{animation:b 1s steps(1) infinite}"
        "</style>",
        f'<rect x="0.5" y="0.5" width="{WIDTH - 1}" height="{height - 1}" rx="10" fill="{BG}" stroke="{BORDER}"/>',
        f'<path d="M0.5 {TITLE_H} V10.5 a10 10 0 0 1 10 -10 H{WIDTH - 10.5} a10 10 0 0 1 10 10 V{TITLE_H} Z" fill="{BAR}"/>',
        f'<line x1="0.5" y1="{TITLE_H}" x2="{WIDTH - 0.5}" y2="{TITLE_H}" stroke="{BORDER}"/>',
        window_buttons(),
        f'<text x="{cx}" y="23" text-anchor="middle" fill="#cfcfcf" style="font-size:12px;font-weight:bold">J0hnwood@ubuntu: ~</text>',
        f'<rect x="1" y="{TITLE_H + 1}" width="{WIDTH - 2}" height="{height - TITLE_H - 2}" fill="url(#vig)"/>',
        f'<text x="{PAD_X}" y="{TITLE_H + 28}" xml:space="preserve">'
        f'<tspan fill="{U_GREEN}">J0hnwood@ubuntu</tspan><tspan fill="{FG}">:</tspan>'
        f'<tspan fill="{U_BLUE}">~</tspan><tspan fill="{FG}">$ ./whoami --banner</tspan></text>',
        f'<text x="{cx}" y="{name_y}" text-anchor="middle" fill="{GREEN}" filter="url(#glow)" style="{big}">J0hnwood</text>',
        f'<text x="{PAD_X}" y="{height - 18}" xml:space="preserve"><tspan fill="{U_GREEN}">J0hnwood@ubuntu</tspan>'
        f'<tspan fill="{FG}">:</tspan><tspan fill="{U_BLUE}">~</tspan><tspan fill="{FG}">$</tspan>'
        f'<tspan class="cur" fill="{GREEN}"> █</tspan></text>',
        f'<rect x="1" y="{TITLE_H + 1}" width="{WIDTH - 2}" height="{height - TITLE_H - 2}" fill="url(#scan)"/>',
        "</svg>",
    ]) + "\n"


if __name__ == "__main__":
    (OUT / "banner.svg").write_text(render_banner(), encoding="utf-8")
    print("wrote assets/banner.svg")
    for name, (title, lines) in BLOCKS.items():
        longest = max((sum(len(t) for t, _ in l) for l in lines), default=0)
        assert longest <= COLS, f"{name}: line of {longest} chars exceeds {COLS}"
        (OUT / f"{name}.svg").write_text(render(title, lines), encoding="utf-8")
        print(f"wrote assets/{name}.svg ({len(lines)} lines, longest {longest})")
