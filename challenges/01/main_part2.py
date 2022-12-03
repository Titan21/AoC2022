

INPUT_FILE = "../02/input.txt"
OUTPUT_FILE = "output_part2.txt"

input = ""

with open(INPUT_FILE, "r") as file:
    input = file.read().splitlines()


calories: list = list()

elve = 0

calories.append({"Elve": elve, "Calories": 0})


for text in input:
    if text == "":
        print(f"Elve {elve:3} has {calories[elve]['Calories']:6} Calories")
        elve += 1
        calories.append({"Elve": elve, "Calories": 0})
        continue
    if text.isnumeric():
        calories[elve]["Calories"] += int(text)
    else:
        print(f"Error: {text}")
        raise Warning("Expecting Numbers")

print("Tallying elves' calories done")

sorted_calories = sorted(calories, key=lambda x: x["Calories"], reverse=True)

print("Sorting elves' calories done")

total_calories = 0
for i in range(0,3):
    total_calories += sorted_calories[i]["Calories"]

with open(OUTPUT_FILE, "w") as file:
    file.write(str(total_calories))

print("Done")