
with open("./challenges/06/input.txt", 'r') as file:
    input = file.readlines()

def find_marker(input):

    for i in range(4, len(input)):
        sequence = input[i-4 :i]

        sequence_set = set(sequence)

        if len(sequence_set) == 4:
            return i

start = find_marker(input[0])

print(start)