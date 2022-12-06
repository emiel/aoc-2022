#!/usr/bin/env python3

from dataclasses import dataclass
import re
import typing as t

MOVE_RE = re.compile(r"^move (?P<count>\d+) from (?P<src>\d) to (?P<dst>\d)$")

Ship: t.TypeAlias = list[list[str]]


@dataclass
class Move:
    count: int
    src: int
    dst: int


@dataclass
class Puzzle:
    ship: Ship
    moves: list[Move]


def parse_drawing(lines: list[str]) -> list[list[str]]:
    result = [[] for i in range(9)]
    for line in reversed(lines):
        assert len(line) > 35
        for col, n in enumerate(range(1, 37, 4)):
            if line[n].isalpha():
                result[col].append(line[n])

    return result


def parse_move(input: str) -> Move:
    match = MOVE_RE.match(input)
    if match is None:
        raise Exception(f"Invalid input: {input}")

    count, src, dst = match.groups()

    return Move(count=int(count), src=int(src), dst=int(dst))


def move_crates_cm9000(ship: Ship, move: Move) -> Ship:
    for n in range(move.count):
        crate = ship[move.src - 1].pop()
        ship[move.dst - 1].append(crate)
    return ship


def move_crates_cm9001(ship: Ship, move: Move) -> Ship:
    src_stack = ship[move.src - 1]
    idx = -move.count
    ship[move.dst - 1].extend(src_stack[idx:])
    del src_stack[idx:]
    return ship


def top_crates(ship: Ship) -> str:
    return "".join(stack[-1] for stack in ship)


def load_input() -> Puzzle:
    ship: Ship = [[]]
    moves = []

    with open("input") as file:
        drawing_lines = []
        for line in file:
            if line.startswith("["):
                drawing_lines.append(line)

            if line == "\n":
                ship = parse_drawing(drawing_lines)

            if line.startswith("move"):
                move = parse_move(input=line.strip())
                moves.append(move)

    return Puzzle(ship=ship, moves=moves)


def part1():
    puzzle = load_input()

    ship = puzzle.ship
    for move in puzzle.moves:
        puzzle.ship = move_crates_cm9000(ship=puzzle.ship, move=move)

    print(f"Part 1 (top crates): {top_crates(ship)}")


def part2():
    puzzle = load_input()

    ship = puzzle.ship
    for move in puzzle.moves:
        puzzle.ship = move_crates_cm9001(ship=puzzle.ship, move=move)

    print(f"Part 2 (top crates): {top_crates(ship)}")


if __name__ == "__main__":
    part1()
    part2()
