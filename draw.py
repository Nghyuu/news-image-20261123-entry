#!/usr/bin/env python3
"""Build-time renderer for the news-image-20261123 entry.

Renders entry.png (1024x1024) from the 10 verified headlines of
Monday 23 November 2026. Runs ONLY at build time; main.ts just copies
the committed PNG. Deterministic: fixed fonts, fixed layout, no
timestamps, no randomness -> byte-identical across runs.
"""
import os
from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)

F_TITLE = lambda s: font("DejaVuSans-Bold.ttf", s)
F_BODY = lambda s: font("DejaVuSans.ttf", s)
F_TAG = lambda s: font("DejaVuSans-Bold.ttf", s)

W, H = 1024, 1024
NAVY = (15, 42, 67)
NAVY2 = (22, 58, 90)
RED = (178, 34, 34)
INK = (24, 24, 24)
GREY = (84, 84, 84)
PAPER = (247, 243, 236)
CARD = (255, 255, 255)
LEAD_BG = (255, 244, 214)
GOLD = (201, 162, 39)
LINE = (210, 204, 192)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

def wrap(text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---- Masthead -------------------------------------------------------
d.rectangle([0, 0, W, 148], fill=NAVY)
d.rectangle([0, 148, W, 154], fill=GOLD)
d.text((36, 22), "MONDAY  •  THE WORLD IN ONE IMAGE", font=F_TAG(20), fill=(180, 205, 225))
d.text((36, 48), "23 NOVEMBER 2026", font=F_TITLE(62), fill=(255, 255, 255))
d.text((36, 118), "Ten stories that defined the day, from Antalya to Washington",
       font=F_BODY(20), fill=(180, 205, 225))

# ---- Lead story -----------------------------------------------------
LX, LY, LW, LH = 36, 172, 952, 196
d.rectangle([LX, LY, LX + LW, LY + LH], fill=LEAD_BG, outline=LINE, width=2)
d.rectangle([LX, LY, LX + 10, LY + LH], fill=RED)
d.text((LX + 28, LY + 16), "LEAD STORY  •  CLIMATE  •  TURKEY", font=F_TAG(19), fill=RED)
lead_head = "COP31 climate summit ends with no deal"
for i, ln in enumerate(wrap(lead_head, F_TITLE(36), LW - 56)):
    d.text((LX + 28, LY + 46 + i * 42), ln, font=F_TITLE(36), fill=INK)
d.text((LX + 28, LY + 138),
       "Talks in Turkey ran to a record length, then collapsed over fossil",
       font=F_BODY(20), fill=GREY)
d.text((LX + 28, LY + 164),
       "fuels and finance. No new pact to tackle climate change.",
       font=F_BODY(20), fill=GREY)

# ---- Grid: 9 stories, 3 x 3 ---------------------------------------
stories = [
    ("MIDDLE EAST", "Iran hits Bahrain as war widens",
     "Iranian attack injures two at a civilian site; Tehran vows to counter a US blockade \u201cby all means\u201d."),
    ("CONFLICT", "Ukraine sinks Russian warship off Libya",
     "Kyiv says naval drones struck the corvette Merkury at Benghazi, carrying the sea war to the Mediterranean."),
    ("USA", "Democrats win biggest House majority since 1992",
     "At least 258 seats called after a recount win in North Carolina\u2019s 5th District."),
    ("MEXICO", "Mexico captures \u2018El Chapo Isidro\u2019",
     "Fausto Isidro Meza Flores, one of the FBI\u2019s 10 most wanted, seized in Sinaloa; more arrests follow."),
    ("ASIA", "South Korea shakes up its cabinet",
     "President Lee announces a surprise reshuffle; the education minister quits over AI exam anti-cheating chaos."),
    ("CYBER", "FBI probes hack of police database",
     "Investigators look into a breach of the National Crime Information Center used by police nationwide."),
    ("TRADE", "EU and Indonesia sign landmark trade deal",
     "A major pact linking Europe with Southeast Asia\u2019s largest economy."),
    ("SPORT", "Skubal signs record $450m Mets deal",
     "Nine years \u2014 the largest contract ever for a pitcher."),
    ("HEALTH \u2022 AFRICA", "Fighting disrupts Ebola response in Congo",
     "WHO says clashes in Ituri forced health workers to shelter as the outbreak response stalls."),
]

GX, GY = 36, 388
CW, CH, GAP = 304, 190, 20
for idx, (tag, head, body) in enumerate(stories):
    r, c = divmod(idx, 3)
    x = GX + c * (CW + GAP)
    y = GY + r * (CH + GAP)
    d.rectangle([x, y, x + CW, y + CH], fill=CARD, outline=LINE, width=2)
    d.rectangle([x, y, x + CW, y + 5], fill=NAVY2)
    d.text((x + 14, y + 16), tag, font=F_TAG(15), fill=RED)
    lines = wrap(head, F_TITLE(21), CW - 28)
    yy = y + 40
    for ln in lines[:3]:
        d.text((x + 14, yy), ln, font=F_TITLE(21), fill=INK)
        yy += 26
    blines = wrap(body, F_BODY(16), CW - 28)
    for ln in blines[:3]:
        d.text((x + 14, yy + 4), ln, font=F_BODY(16), fill=GREY)
        yy += 21

# ---- Footer ---------------------------------------------------------
d.text((36, 1004), "Sources: Just Security \u2022 AFP \u2022 UN News \u2022 Reuters \u2022 Off the Wire  \u2014  23 Nov 2026",
       font=F_BODY(14), fill=GREY)

img.save(OUT, format="PNG", optimize=True)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
