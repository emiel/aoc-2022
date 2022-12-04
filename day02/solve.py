#!/usr/bin/env python3
from typing import Iterator

import enum


class Move(enum.Enum):
    ROCK = 0
    PAPER = 1
    SCISSOR = 2


class Outcome(enum.Enum):
    LOSE = 0
    DRAW = 1
    WIN = 2


def parse_move(input: str) -> Move:
    return {
        "A": Move.ROCK,
        "B": Move.PAPER,
        "C": Move.SCISSOR,
        "X": Move.ROCK,
        "Y": Move.PAPER,
        "Z": Move.SCISSOR,
    }[input]


def parse_outcome(input: str) -> Outcome:
    return {
        "X": Outcome.LOSE,
        "Y": Outcome.DRAW,
        "Z": Outcome.WIN,
    }[input]


MOVE_POINTS = {
    Move.ROCK: 1,
    Move.PAPER: 2,
    Move.SCISSOR: 3,
}

MOVES_WIN = {
    Move.PAPER: Move.SCISSOR,
    Move.ROCK: Move.PAPER,
    Move.SCISSOR: Move.ROCK,
}

MOVES_LOSE = {
    Move.PAPER: Move.ROCK,
    Move.ROCK: Move.SCISSOR,
    Move.SCISSOR: Move.PAPER,
}


def play_round_part1(op_move: Move, my_move: Move) -> int:
    points = MOVE_POINTS[my_move]

    # Draw
    if op_move == my_move:
        return points + 3

    # Opponent wins
    if (
        (op_move == Move.ROCK and my_move == Move.SCISSOR)
        or (op_move == Move.SCISSOR and my_move == Move.PAPER)
        or (op_move == Move.PAPER and my_move == Move.ROCK)
    ):
        return points

    # My win
    return points + 6


def play_round_part2(op_move: Move, outcome: Outcome) -> int:
    if outcome == Outcome.LOSE:
        my_move = MOVES_LOSE[op_move]
        return MOVE_POINTS[my_move] + 0

    if outcome == Outcome.DRAW:
        my_move = op_move
        return MOVE_POINTS[my_move] + 3

    if outcome == Outcome.WIN:
        my_move = MOVES_WIN[op_move]
        return MOVE_POINTS[my_move] + 6

    raise Exception("Unsupported outcome")


def load_strategy_guide(filename: str) -> Iterator[tuple[Move, Outcome]]:
    with open(filename) as file:
        for line in file:
            op_move, my_move_or_outcome = line.strip().split(" ", maxsplit=2)
            yield parse_move(op_move), parse_outcome(my_move_or_outcome)


if __name__ == "__main__":
    game_points = 0

    for op_move, outcome in load_strategy_guide("./input"):
        round_points = play_round_part2(op_move, outcome)
        game_points += round_points

    print(f"Your total score: {game_points}")
