import os

SCORES = {"X": 0, "Y": 3, "Z": 6, "rock": 1, "paper": 2, "scissors": 3}

LOOKUP = {
    "A": {
        "name": "rock",
        "losesto": "B",
        "beats": "C"
    },
    "B": {
        "name": "paper",
        "losesto": "C",
        "beats": "A"
    },
    "C": {
        "name": "scissors",
        "losesto": "A",
        "beats": "B"
    },
}

with open(os.path.join(os.getcwd(), "input.txt"), "r") as guide:
    score = 0
    line = guide.readline()
    while line:
        result = tuple(line.rstrip("\n").split())
        print(result)
        score += SCORES[result[1]]
        if result[1] == "Y":
            score += SCORES[LOOKUP[result[0]]["name"]]
        if result[1] == "Z":
            score += SCORES[LOOKUP[LOOKUP[result[0]]["losesto"]]["name"]]
        if result[1] == "X":
            score += SCORES[LOOKUP[LOOKUP[result[0]]["beats"]]["name"]]
        line = guide.readline()

print(score)
