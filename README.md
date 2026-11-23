# news-image-20261123 entry

One image summing up the world's news of **Monday 23 November 2026**,
built for the make.fun competition
[news-image-20261123](https://make.fun/bounty/news-image-20261123)
(pool $100).

## The image

A newspaper front page, drawn from scratch with PIL (`draw.py` — every
shape is a geometric drawing, no photo or internet image is used):

- Masthead **THE WORLD TODAY** with the date banner
  **MONDAY 23 NOVEMBER 2026** in large type.
- Headline story: **CLIMATE TALKS COLLAPSE** — COP31 in Antalya ends
  with no deal after the fossil-fuel wording is dropped, the longest
  COP on record (CNN / Reuters, 22 Nov 2026).
- Four panels (2×2):
  1. **GULF WAR FLARES** — Iran hits US bases in Bahrain; tankers
     struck in the Strait of Hormuz (Al Jazeera / Reuters, 21–22 Nov 2026).
  2. **RUSSIAN WARSHIP SUNK** — Ukrainian drones sink the corvette
     *Merkury* off Libya and hit the cargo ship *Sparta II* in the
     Baltic (WSJ / The Times, 22 Nov 2026).
  3. **DEMOCRATS TAKE HOUSE** — 258 seats, the biggest US House
     majority since 1992 (AP / Reuters, 22 Nov 2026).
  4. **FACTORY FIRE IN JAVA** — 3 dead, dozens missing after the
     candy-factory fire in Banten, Indonesia (AP / BBC, 22 Nov 2026).

## How it runs

`main.py` (Python 3, standard library only, no network) validates the
bundled `entry.png` (PNG, ≤ 1 MiB, ≤ 1024×1024) and copies it to
`$MAKEFUN_OUTPUT_DIR/entry.png` with mode 0644. Two runs write the
same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`draw.py` regenerates `entry.png` from scratch (needs Pillow, build
time only — it is not run by the grader).

## License

MIT — see [LICENSE](LICENSE).
