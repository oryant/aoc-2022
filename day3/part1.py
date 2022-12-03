import os


def letter_priority(letter: str) -> int:
    if letter == letter.upper():
        return ord(letter) - 38
    else:
        return ord(letter) - 96


def process_rucksack(rucksack: str) -> int:  # type: ignore
    for letter in rucksack[: len(rucksack) // 2]:
        if letter in rucksack[len(rucksack) // 2 :]:  # noqa: E203
            return letter_priority(letter)


with open(os.path.join(os.getcwd(), "input.txt"), "r") as rucksacks:
    print(sum([process_rucksack(line) for line in rucksacks.readlines()]))
