import os


def letter_priority(letter: str) -> int:
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def process_group(group: list) -> int:  # type: ignore
    assert len(group) == 3
    common_letter = set(group[0]).intersection(group[1], group[2])
    return letter_priority(list(common_letter)[0])


with open(os.path.join(os.getcwd(), "input.txt"), "r") as rucksacks:
    lines = rucksacks.readlines()
    result = 0
    while lines:
        group = [lines.pop().rstrip("\n") for x in range(3)]
        result += process_group(group)

print(result)
