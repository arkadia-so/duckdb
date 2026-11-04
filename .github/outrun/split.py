#!/usr/bin/env python3
"""split.py <list> <shard> <shards>: shard <shard> (1-based) of a unittest --list-tests output, round-robin.

ARK-81 bench (outrun): workflow-level sharding until outrun has a duration-balanced shard command.
Keeps the list's format (name<TAB>group) and its header, which run_tests.py's load_tests skips.
"""
import sys

path, shard, shards = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
lines = [l.rstrip("\n") for l in open(path, encoding="utf8", errors="replace")]
tests = [l for l in lines if l and l != "name\tgroup"]
mine = tests[shard - 1 :: shards]
print("name\tgroup")
print("\n".join(mine))
print(f"shard {shard}/{shards}: {len(mine)} of {len(tests)} tests", file=sys.stderr)
