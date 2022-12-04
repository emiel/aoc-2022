#!/usr/bin/env python3
import itertools


def _parse_pack(line: str) -> tuple[str, str]:
    compartment_count = len(line) // 2
    return line[:compartment_count], line[compartment_count:]


def _lookup_priority(chr: str) -> int:
    if chr.islower():
        return ord(chr) - 96
    else:
        return ord(chr) - 38


def _process_pack(comp1: str, comp2: str) -> int:
    common = set(comp1).intersection(set(comp2))
    assert len(common) == 1
    chr: str = common.pop()
    return _lookup_priority(chr)


def _load_packs():
    with open("input") as file:
        for line in file:
            yield _parse_pack(line.strip())


def part1():
    total = 0
    for c1, c2 in _load_packs():
        priority = _process_pack(c1, c2)
        total += priority

    print(f"Total part 1: {total}")


def _groups():
    with open("input") as file:
        iterable = iter(file)
        while chunk := list(itertools.islice(iterable, 3)):
            yield [grp.strip() for grp in chunk]


def part2():
    total = 0
    for sack1, sack2, sack3 in _groups():
        common = set(sack1).intersection(set(sack2), set(sack3))

        assert len(common) == 1
        badge = common.pop()
        priority = _lookup_priority(badge)
        total += priority
    print(f"Total part 2: {total}")


if __name__ == "__main__":
    part1()
    part2()
