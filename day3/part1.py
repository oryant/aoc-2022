import os


def letter_priority(letter: str) -> int:
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def process_rucksack(rucksack: str) -> int:  # type: ignore
    common_letter = set(rucksack[: len(rucksack) // 2]).intersection(
        rucksack[len(rucksack) // 2 :]
    )
    return letter_priority(list(common_letter)[0])


with open(os.path.join(os.getcwd(), "input.txt"), "r") as rucksacks:
    print(sum([process_rucksack(line) for line in rucksacks.readlines()]))
