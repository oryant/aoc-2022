import os

SCORES = {"win": 6, "draw": 3, "lose": 0}

LOOKUP = {
    "X": {
        "name": "rock",
        "value": 1,
        "scoresagainst": {
            "A": SCORES["draw"],
            "B": SCORES["lose"],
            "C": SCORES["win"],
        },
    },
    "Y": {
        "name": "paper",
        "value": 2,
        "scoresagainst": {
            "A": SCORES["win"],
            "B": SCORES["draw"],
            "C": SCORES["lose"],
        },
    },
    "Z": {
        "name": "scissors",
        "value": 3,
        "scoresagainst": {
            "A": SCORES["lose"],
            "B": SCORES["win"],
            "C": SCORES["draw"],
        },
    },
}

with open(os.path.join(os.getcwd(), "input.txt"), "r") as guide:
    score = 0
    line = guide.readline()
    while line:
        result = tuple(line.rstrip("\n").split())
        print(result)
        score += (
            LOOKUP[result[1]]["value"] + LOOKUP[result[1]]["scoresagainst"][result[0]]
        )
        line = guide.readline()

print(score)
