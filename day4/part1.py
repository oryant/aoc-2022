import os


def parse_line(line: str) -> list[list]:
    pairs = [rng.split("-") for rng in line.split(",")]
    return [ [ int(a) for a in pair ] for pair in pairs ]


def compare_assignments(pair: list[list]) -> bool:
    pair = sorted(pair, key=lambda a: len(range(*a)), reverse=True)
    result =  (int(pair[0][0]) <= int(pair[1][0])) and (int(pair[0][1]) >= int(pair[1][1]))
    print(pair, result)
    return result

with open(os.path.join(os.getcwd(), "input.txt"), "r") as sections:
    print(sum([compare_assignments(parse_line(line.rstrip("\n"))) for line in sections.readlines()]))
