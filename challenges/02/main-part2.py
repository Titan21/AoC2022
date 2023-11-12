from enum import Enum

class ShapeScores(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class MatchScores(Enum):
    Loss = 0
    Draw = 3
    Win = 6

points = {
    "A": {
        "X": MatchScores.Draw.value + ShapeScores.Rock.value,
        "Y": MatchScores.Win.value + ShapeScores.Paper.value,
        "Z": MatchScores.Loss.value + ShapeScores.Scissors.value
    },
    "B": {
        "X": MatchScores.Loss.value + ShapeScores.Rock.value,
        "Y": MatchScores.Draw.value + ShapeScores.Paper.value,
        "Z": MatchScores.Win.value + ShapeScores.Scissors.value
    },
    "C": {
        "X": MatchScores.Win.value + ShapeScores.Rock.value,
        "Y": MatchScores.Loss.value + ShapeScores.Paper.value,
        "Z": MatchScores.Draw.value + ShapeScores.Scissors.value
    },
}

# A|X = Rock
# B|Y = Paper
# C|Z = Scissors

results = {
    "A": {
        # Loose
        "X": "Z",
        # Draw
        "Y": "X",
        # Win
        "Z": "Y"
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z"
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X"
    },
}

with open('./challenges/02/input.txt', 'r') as file:
    input = file.read().splitlines()

scores = []

for line in input:
    theirs, target_result = line.split(" ")

    tool = results[theirs][target_result]

    score = points[theirs][tool]
    scores.append(score)
    print(score)

print(f"Total: {sum(scores)}")