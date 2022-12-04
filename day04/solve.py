#!/usr/bin/env python3

from dataclasses import dataclass


@dataclass
class Assignment:
    lb: int
    ub: int


def parse_assignment(input: str) -> Assignment:
    lb, ub = input.split("-", 2)
    return Assignment(lb=int(lb), ub=int(ub))


def fully_contains(a: Assignment, b: Assignment) -> bool:
    return a.lb >= b.lb and a.ub <= b.ub


def overlap(a: Assignment, b: Assignment) -> bool:
    return a.lb <= b.ub and a.ub >= b.lb


def solve():
    with open("input") as file:
        contains_count = 0
        overlap_count = 0
        for line in file:
            line = line.strip()
            part1, part2 = line.split(",", 2)
            a1 = parse_assignment(part1)
            a2 = parse_assignment(part2)

            if fully_contains(a1, a2) or fully_contains(a2, a1):
                contains_count += 1
            if overlap(a1, a2):
                overlap_count += 1

        print(f"Total contains count (part1): {contains_count}")
        print(f"Total overlap count (part2): {overlap_count}")


if __name__ == "__main__":
    solve()
