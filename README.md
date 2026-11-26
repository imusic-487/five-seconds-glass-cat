# Five Seconds to Explain the Glass

[![make.fun](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![rank](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/imusic-487/five-seconds-glass-cat/rank.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)
[![reward](https://make.fun/badge/u-po-pu-five-seconds-to-explain-the-glass-934d9949/imusic-487/five-seconds-glass-cat/reward.svg)](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949)

Entry for the [Five Seconds to Explain the Glass](https://make.fun/bounty/u-po-pu-five-seconds-to-explain-the-glass-934d9949) bounty on [make.fun](https://make.fun).

## The entry

`main.py` writes the one sentence a house cat says in its own defence,
five seconds after knocking a glass off the table, to `/output/entry.txt`:

> The glass was squatting in my sunbeam rent-free, so I evicted it — the shards are its deposit and the floor is its new address.

One sentence, 127 characters, in the cat's own voice: self-interest
(the sunbeam, the rent), zero remorse, no apology and no confession —
and a fresh eviction joke, not the gravity, slippery-edge or
it-was-already-falling lines.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: a fixed string, standard library only, no network,
no randomness, no environment input. Every run writes the same bytes.

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
