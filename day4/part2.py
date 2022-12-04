import os


def parse_line(line: str) -> list[list]:
    pairs = [rng.split("-") for rng in line.split(",")]
    return [[int(a) for a in pair] for pair in pairs]


def inclusive_range(start: int, stop: int) -> range:
    return range(start, stop + 1)


def compare_assignments(pair: list[list]) -> bool:
    pair = sorted(
        pair, key=lambda a: len(range(*a)), reverse=True
    )  # sort by size of range
    result = bool(
        set(inclusive_range(*pair[0])).intersection(inclusive_range(*pair[1]))
    )
    return result


with open(os.path.join(os.getcwd(), "input.txt"), "r") as sections:
    print(
        sum(
            [
                compare_assignments(parse_line(line.rstrip("\n")))
                for line in sections.readlines()
            ]
        )
    )
