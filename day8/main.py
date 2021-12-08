def read_data(filename):
    with open(filename, 'r') as f:
        for line in f:
            [idata, odata] = line.split('|')
            inputs.append(convert_to_list(idata.strip()))
            outputs.append(convert_to_list(odata.strip()))


def convert_to_list(line):
    v = []
    for word in line.split(' '):
        v.append(''.join(sorted(word)))
    return v


def count_output(outputs):
    total = 0
    for vector in outputs:
        for output in vector:
            size = len(output)
            if size != 5 and size != 6:
                total += 1
    return total


def fill_known_digits(vector):
    digits = ['' for _ in range(10)]
    for element in vector:
        size = len(element)
        if size == 2:
            digits[1] = element
        elif size == 4:
            digits[4] = element
        elif size == 3:
            digits[7] = element
        elif size == 7:
            digits[8] = element
    return digits


def contains(string, sub):
    return set(sub).issubset(set(string))


def fill_unknown_digits(vector, digits):
    candidates = []
    for element in vector:
        if len(element) == 5 or len(element) == 6:
            candidates.append(element)

    e3 = [element for element in candidates if len(element) == 5 and contains(element, digits[1])]
    candidates.remove(e3[0])
    e9 = [element for element in candidates if len(element) == 6 and contains(element, e3[0])]
    candidates.remove(e9[0])
    e0 = [element for element in candidates if len(element) == 6 and contains(element, digits[1]) and element != e9[0]]
    candidates.remove(e0[0])
    e6 = [element for element in candidates if len(element) == 6]
    candidates.remove(e6[0])
    e5 = [element for element in candidates if len(element) == 5 and contains(e6[0], element)]
    candidates.remove(e5[0])
    e2 = [element for element in candidates if len(element) == 5]

    digits[0] = e0[0]
    digits[2] = e2[0]
    digits[3] = e3[0]
    digits[5] = e5[0]
    digits[6] = e6[0]
    digits[9] = e9[0]

    return digits


def get_output_values():
    total_sum = 0
    for idx, vector in enumerate(inputs):
        digits = fill_known_digits(vector)
        digits = fill_unknown_digits(vector, digits)
        value = []
        for output in outputs[idx]:
            value.append(str(digits.index(output)))
        val_num = int(''.join(value))
        total_sum += val_num
    return total_sum


if __name__ == "__main__":
    file_name = "input.txt"
    # file_name = "test.txt"
    inputs = []
    outputs = []
    read_data(file_name)

    # Part 1
    print("Part 1:", count_output(outputs))

    # Part 2
    output_values = get_output_values()
    print("Part 2:", output_values)
