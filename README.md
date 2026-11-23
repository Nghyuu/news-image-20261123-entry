# news-image-20261123 — 23 November 2026 in one image

[![news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Nghyuu/news-image-20261123-entry/rank.svg)](https://make.fun/bounty/news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Nghyuu/news-image-20261123-entry/reward.svg)](https://make.fun/bounty/news-image-20261123)

[Bounty: news-image-20261123 — "Sum up 23 November's world news in one image"](https://make.fun/bounty/news-image-20261123)

## The image

One 1024×1024 PNG summing up Monday 23 November 2026: the COP31 climate
summit collapsing without a deal leads, with nine more verified stories from
the day in a grid — the Iran war widening to Bahrain, Ukraine sinking a
Russian warship off Libya, the Democrats' biggest House majority since 1992,
Mexico capturing "El Chapo Isidro", South Korea's cabinet reshuffle, the FBI
probing a hack of the national police database, an EU–Indonesia trade deal,
Skubal's record $450m Mets contract, and fighting disrupting the Ebola
response in Congo.

## How it is built

- `draw.py` (build time only, Pillow/DejaVu) renders `entry.png` from the
  ten verified headlines. It runs twice byte-identical.
- `main.ts` (Node 22, stdlib only) copies the committed `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`. It never shells out and never uses the
  network.

## Sources (23 Nov 2026)

Just Security (Early Edition, 23 Nov 2026), AFP, UN News, Reuters,
Off the Wire, 10 Things Global News, The Russell Record.
