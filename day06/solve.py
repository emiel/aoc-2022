#!/usr/bin/env python3


def solve(buf: str, distinct_count: int) -> int | None:
    for i in range(len(buf)):
        window = buf[i : i + distinct_count]
        if len(set(window)) == distinct_count:
            return i + distinct_count


def main():
    with open("./input") as file:
        buf = file.read()

        start_of_packet = solve(buf, distinct_count=4)
        print(f"Part 1: {start_of_packet}")

        start_of_message = solve(buf, distinct_count=14)
        print(f"Part 2: {start_of_message}")


if __name__ == "__main__":
    main()
