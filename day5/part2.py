import os

ship = {
    "1": ["R", "G", "H", "Q", "S", "B", "T", "N"],
    "2": ["H", "S", "F", "D", "P", "Z", "J"],
    "3": ["Z", "H", "V"],
    "4": ["M", "Z", "J", "F", "G", "H"],
    "5": ["T", "Z", "C", "D", "L", "M", "S", "R"],
    "6": ["M", "T", "W", "V", "H", "Z", "J"],
    "7": ["T", "F", "P", "L", "Z"],
    "8": ["Q", "V", "W", "S"],
    "9": ["W", "H", "L", "M", "T", "D", "N", "C"],
}


def parse_line(line: str) -> list:
    parsed = line.rstrip("\n").split()
    output = []
    for item in parsed:
        try:
            output.append(int(item))
        except ValueError:
            pass
    return output


def get_top_crates() -> str:
    return str([ship[f"{i}"][-1] for i in range(1, len(ship) + 1)])


def move_crates(moves: list) -> None:
    print(f"Executing {moves[0]} moves")
    moved_crates = ship[str(moves[1])][-abs(moves[0]) :]
    del ship[str(moves[1])][-abs(moves[0]) :]
    ship[str(moves[2])].extend(moved_crates)


with open(os.path.join(os.getcwd(), "input.txt"), "r") as procedures:
    linecount = 1
    for line in procedures.readlines():
        print(f"Processing line {linecount}")
        print(f"Current state: { {k: len(v) for k, v in ship.items()} }")
        move_crates(parse_line(line))
        linecount += 1

print(get_top_crates())
