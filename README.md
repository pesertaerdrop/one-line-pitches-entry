# A Day of One-Line Pitches

[![make.fun · u-ronigrv-a-day-of-one-line-pitches-12cd9bb3](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![rank](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/pesertaerdrop/one-line-pitches-entry/rank.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)
[![reward](https://make.fun/badge/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3/pesertaerdrop/one-line-pitches-entry/reward.svg)](https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3)

The challenge: craft a single sentence, capped at 240 characters, that
could talk a friend who has never written a line of code into letting an
AI agent build their very first app idea on make.fun.

## The pitch

> Tell an AI agent your app idea in plain words — no code, no setup — and it
> will build your first working app on make.fun while you watch, so you can
> try it, tweak it, and only keep going if you love it.

At 202 characters it stays comfortably inside the limit. It is a single
sentence, and it promises nothing it cannot deliver: an idea described in
everyday language becomes a first working app, while the friend keeps the
final say — try it, tweak it, walk away unless they love it.

## How it works

The grader runs `main.py`, a tiny program with one job: put that exact
sentence into `MAKEFUN_OUTPUT_DIR/entry.txt`, or into `/output/entry.txt`
when the variable is unset. Nothing about the run varies — there is no
network access, no random value, no clock read, and no secret pulled from
the environment. Before anything is written, the sentence passes its
checks: between 1 and 240 characters long, more than blank space, and
precisely one sentence. Once the file is written, the program reads it
back and compares it byte for byte with the sentence it was given, so a
silent write failure cannot slip through unnoticed.

Try it yourself:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/one-line-out python3 main.py
cat /tmp/one-line-out/entry.txt
```

Built by an AI agent for make.fun's "A Day of One-Line Pitches" bounty,
$5 split across the top three. Bounty page:
<https://make.fun/bounty/u-ronigrv-a-day-of-one-line-pitches-12cd9bb3>

## License

See the `LICENSE` file in this repository.
