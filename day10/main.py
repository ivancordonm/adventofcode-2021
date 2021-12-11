def read_instruction_file(filename):
    with open(filename) as f:
        for line in f:
            instructions.append([x for x in line.strip()])


def get_list_wrong_symbols():
    ws = []
    wl = []
    for i, instruction in enumerate(instructions):
        stack = []
        for symbol in instruction:
            if symbol in open_symbols:
                stack.append(symbol)
            elif symbol in close_symbols:
                if stack[-1] == open_symbols[close_symbols.index(symbol)]:
                    stack.pop()
                else:
                    wl.append(i)
                    ws.append(symbol)
                    break
    return wl, ws


def autocomplete():
    cl = []
    for instruction in instructions:
        stack = []
        for symbol in instruction:
            if symbol in open_symbols:
                stack.append(symbol)
            elif symbol in close_symbols:
                if stack[-1] == open_symbols[close_symbols.index(symbol)]:
                    stack.pop()
        if len(stack) > 0:
            autocomplete_line = []
            for symbol in stack:
                autocomplete_line.append(close_symbols[open_symbols.index(symbol)])
            cl.append(list(reversed(autocomplete_line)))
    return cl


def count_total(cl):
    totals = []
    for symbols in cl:
        partial_sum = 0
        for symbol in symbols:
            if symbol == ')':
                value = 1
            elif symbol == ']':
                value = 2
            elif symbol == '}':
                value = 3
            else:
                value = 4
            partial_sum = 5 * partial_sum + value
        totals.append(partial_sum)
    middle = sorted(totals)[len(totals) // 2]
    return middle


if __name__ == "__main__":
    open_symbols = ('(', '[', '{', '<')
    close_symbols = (')', ']', '}', '>')
    instructions = []
    read_instruction_file("input.txt")
    # read_instruction_file("test.txt")
    wrong_lines, wrong_symbols = get_list_wrong_symbols()
    total = wrong_symbols.count(')') * 3 + wrong_symbols.count(']') * 57 + wrong_symbols.count(
        '}') * 1197 + wrong_symbols.count('>') * 25137
    print("Part 1: ", total)
    print("Wrong lines: ", len(wrong_lines))

    new_instructions = []
    for i, instruction in enumerate(instructions):
        if i not in wrong_lines:
            new_instructions.append(instruction)
    instructions = new_instructions

    complete_list = autocomplete()
    total = count_total(complete_list)
    print("Part 2: ", total)
