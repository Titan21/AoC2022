
with open("./challenges/06/input.txt", 'r') as file:
    input = file.readlines()

def find_marker(input, length):

    for i in range(length, len(input)):
        sequence = input[i-length :i]

        sequence_set = set(sequence)

        if len(sequence_set) == length:
            return i

start = find_marker(input[0], 14)

print(start)