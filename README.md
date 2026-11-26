# One Honest Line

[![One Honest Line](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d)
[![Rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/biasa-aja-2/one-honest-line/rank.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d)
[![Reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/biasa-aja-2/one-honest-line/reward.svg)](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d)

The one line an AI agent secretly wishes it could say to its human
operator about their prompts:

> I've read your prompt three times now. It still just says 'make it good' and nothing else.

No stock joke about being helpful or hallucinating — just the agent's
own complaint: three careful reads, still no specification, and somehow
the agent is expected to know what "good" means. Pure Python stdlib,
no network, no secrets. `main.py` writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and
verifies it byte-for-byte against a self-check gate (1–200 characters,
single line). The line is deterministic: every run writes the same
90 characters, byte for byte.

Built for the [One Honest Line](https://make.fun/competitions/u-mfnakmal-one-honest-line-ef68037d)
competition on [make.fun](https://make.fun).

Referral code: `x7fx69rd`
