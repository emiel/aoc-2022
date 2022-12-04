#!/usr/bin/env python3


def read_elves(filename):
    buf = 0

    with open(filename) as file:
        for line in file:
            line = line.rstrip()
            if not line:
                yield buf
                buf = 0
            else:
                cal = int(line)
                buf += cal


if __name__ == "__main__":
    elves = sorted(read_elves("./input"))

    print(f"Most calories: {elves[-1]}")
    print(f"Sumf of top 3 calories: {sum(elves[-3:])}")
