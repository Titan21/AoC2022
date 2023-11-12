

with open("./challenges/04/input.txt", "r") as file:
    pairs = file.read().splitlines()


def inclusiveRange(*args):
    return range(args[0], args[1] + 1)

counter = 0

for pair in pairs:

    short1, short2 = pair.split(',')

    sections1 = set(inclusiveRange(*[int(i) for i in short1.split("-")]))
    sections2 = set(inclusiveRange(*[int(i) for i in short2.split("-")]))

    overlap = sections1 & sections2

    if len(overlap) > 0:
        counter = counter + 1


print(f"Total Overlap: {counter}")
    