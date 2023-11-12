from dataclasses import dataclass
from typing import List

with open("./challenges/05/input.txt", "r") as file:
    input = file.read().splitlines()

width = -1
section = 'layout'
layout = []
string_instructions = []

for line in input:

    if line == "":
        section = "instructions"
        continue

    if section == 'layout':
        width = int((len(line) + 1) / 4)
        layout.append(line)
    elif section == 'instructions':
        string_instructions.append(line)

def parse_container_layout(data, width):

    stacks = []
    for column in range(width):
        stacks.append(list())


    # Clear last line in data
    data.pop()

    for row in reversed(data):
        for column, character_index in enumerate(range(1, 4 * width, 4)):
            for container in row[character_index]:
                if container != " ":
                    stacks[column].append(container)

    return stacks

@dataclass
class Instuction:
    amount: int
    pos_from: int
    pos_to: int

    def __post_init__(self):
        self.amount = int(self.amount)
        self.pos_from = int(self.pos_from)
        self.pos_to = int(self.pos_to)

def parse_instructions(data) -> List[Instuction]:

    instructions = []
    for line in data:

        parts = line.split(" ")
        instructions.append(Instuction(parts[1], parts[3], parts[5]))
    return instructions

def move(layout, pos_from, pos_to):

    moving = layout[pos_from - 1].pop()
    layout[pos_to - 1].append(moving)
    return layout

def perform_operations(layout: List[str], instructions: List[Instuction]):

    for instruction in instructions:

        print(f"Before Instruction: {layout}")
        for _ in range(instruction.amount):
            layout = move(layout, instruction.pos_from, instruction.pos_to)
        print(f"After instruction: {layout}")

stacks = parse_container_layout(layout, width)
instructions = parse_instructions(string_instructions)

perform_operations(stacks, instructions)

print("Final Layout:")
for stack in stacks:
    print(f"{stack.pop()}", end="")

print("yaout done")