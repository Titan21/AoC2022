import string
from itertools import batched

with open("./challenges/03/input.txt", "r") as file:
    rucksacks = file.read().splitlines()

priorities = []

for group_rucksacks in batched(rucksacks, n=3):
    sacks = [set(strings) for strings in group_rucksacks]

    intersection = set.intersection(*sacks)
    intersection_letter = intersection.pop()

    priority = string.ascii_letters.index(intersection_letter) + 1

    priorities.append(priority)

print(f"Final result is: {sum(priorities)}")