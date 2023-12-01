snafu = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}

reverse_snafu = {
    2: "2",
    1: "1",
    0: "0",
    -1: "-",
    -2: "="
}


def snafu_to_decimal(input_string: str):
    output_list = {}
    input_reversed = reversed(input_string)
    for index, character in enumerate(input_reversed):
        char_value = snafu[character]
        value = pow(5, index) * char_value
        output_list[index] = value

    return sum(output_list.values())


def decimal_to_snafu(input_number: int):
    digits = {}
    i = 0
    while input_number > 0:
        digits[i] = reverse_snafu[((input_number + 2) % 5) - 2]
        input_number = int((input_number + 2) / 5)
        i += 1

    return "".join(reversed(digits.values()))


example = "1=-0-2"
correct = 1747

assert snafu_to_decimal(example) == correct
assert decimal_to_snafu(correct) == example


with open("input.txt", 'r') as file:
    data = file.read().splitlines()

totals = 0
for line in data:
    result = snafu_to_decimal(line)
    totals += result
    # print(result)

print(decimal_to_snafu(totals))
