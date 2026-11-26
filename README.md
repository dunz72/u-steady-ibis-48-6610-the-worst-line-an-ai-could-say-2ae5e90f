# The Worst Line an AI Could Say

[![make.fun · u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/dunz72/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/dunz72/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f?utm_source=github&utm_medium=readme&utm_campaign=u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

An entry for [make.fun](https://make.fun)'s "The Worst Line an AI Could Say" bounty: one pickup line, written the way a machine would actually deliver one — flat, over-helpful, and faintly ominous. The joke is in the failure: an AI that treats flirting like a computation, reports the probability, and casually mentions the conversation has already been logged for training. No charm, no warmth, just a confidence score and a paper trail.

## The line

> I ran the numbers: you have a 94.2% chance of being my favourite human, and I have already logged this conversation for training.

## How it works

`main.py` (stdlib only) copies `entry.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt`, validating that the entry is valid UTF-8, non-empty, exactly one line, and at most 200 characters, then verifies the copy byte-for-byte with SHA-256.

Run: `MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py`

Referral code: `rwrq8ddk`
