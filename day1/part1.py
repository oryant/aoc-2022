import os

print(os.getcwd())

with open(os.path.join(os.getcwd(), "input.txt"), "r") as numbers:
    elves = []
    calories = 0
    line = numbers.readline()
    print(line)
    while line:
        try:
            calories = calories + int(line.rstrip('\n'))
        except ValueError:
            elves.append(calories)
            calories = 0
        line = numbers.readline()

print(max(elves))
