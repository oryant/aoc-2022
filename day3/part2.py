import os


def letter_priority(letter: str) -> int:
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def process_group(group: list) -> int:  # type: ignore
    assert len(group) == 3
    for letter in group[0]:
        if letter in group[1] and letter in group[2]:
            return letter_priority(letter)


with open(os.path.join(os.getcwd(), "input.txt"), "r") as rucksacks:
    lines = rucksacks.readlines()
    result = 0
    while lines:
        group = [lines.pop() for x in range(3)]
        result += process_group(group)

print(result)
