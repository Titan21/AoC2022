

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_part1.txt"

input = ""

with open(INPUT_FILE, "r") as file:
    input = file.read().splitlines()


calories: list = list()
calories.append(0)

elve = 0

max_calories = -1
max_elve = -1
for text in input:
    if text == "":
        print(f"Elve {elve:3} has {calories[elve]:6} Calories")
        if calories[elve] > max_calories:
            max_elve = elve
            max_calories = calories[elve]
        calories.append(0)
        elve += 1
        continue
    if text.isnumeric():
        calories[elve] += int(text)
    else:
        print(f"Error: {text}")
        raise Warning("Expecting Numbers")

print(f"Elve {max_elve} has max Calories: {max_calories}")

with open(OUTPUT_FILE, "w") as file:
    file.write(str(max_calories))

print("Done")