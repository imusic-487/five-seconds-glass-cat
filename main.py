#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the one sentence a house cat says in its own defence, five
seconds after knocking a glass off the table, to /output/entry.txt.

Deterministic: a fixed string, standard library only, no network,
no randomness, no environment input. Every run writes the same bytes.
"""

import os

ENTRY = "The glass was squatting in my sunbeam rent-free, so I evicted it — the shards are its deposit and the floor is its new address."
# One sentence, 127 characters, in the cat's own voice: self-interest
# (sunbeam, rent), zero remorse, no apology or confession, and a fresh
# eviction joke — no gravity, slippery-edge or already-falling line.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
