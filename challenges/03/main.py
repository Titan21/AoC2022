import string

with open("./challenges/03/input.txt", "r") as file:
    rucksacks = file.read().splitlines()

priorities = []

for rucksack in rucksacks:
    half_length = int(len(rucksack)/2)
    comp1 = rucksack[:half_length]
    comp2 = rucksack[half_length:]

    comp1set = set(comp1)
    comp2set = set(comp2)

    intersection = comp1set & comp2set
    intersection_letter = intersection.pop()

    priority = string.ascii_letters.index(intersection_letter) + 1

    priorities.append(priority)

print(f"Final result is: {sum(priorities)}")