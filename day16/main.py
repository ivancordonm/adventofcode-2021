def read_input(filename):
    return [x for x in open(filename).read().strip()]


def analize_packet(idx, versions):
    l_idx = 0
    # version
    v = int(transmision_b[idx + l_idx:idx + l_idx + 3], 2)
    l_idx += 3
    # type
    t = int(transmision_b[idx + l_idx:idx + l_idx + 3], 2)
    l_idx += 3

    # literal
    if t == 4:
        last = False
        while not last:
            last = transmision_b[idx + l_idx] == '0'
            l_idx += 5
        return versions + [v], l_idx
    else:
        type_length = transmision_b[idx + l_idx]
        if type_length == '0':
            l_idx += 1
            length = int(transmision_b[idx + l_idx:idx + l_idx + 15], 2)
            processed = 0
            l_idx += 15
            while processed < length:
                versions, p = analize_packet(idx + l_idx, versions)
                l_idx += p
                processed += p
            return versions + [v], l_idx
        else:
            l_idx += 1
            packets = int(transmision_b[idx + l_idx:idx + l_idx + 11], 2)
            l_idx += 11
            processed = 0
            for i in range(packets):
                versions, p = analize_packet(idx + l_idx, versions)
                l_idx += p
                processed += p
            return versions + [v], l_idx


def tr(t):
    if t == 0:
        return 'sum'
    elif t == 1:
        return 'mul'
    elif t == 2:
        return 'min'
    elif t == 3:
        return 'max'
    elif t == 5:
        return 'gt'
    elif t == 6:
        return 'lt'
    elif t == 7:
        return 'eq'


def calculate(idx, op):
    l_idx = 0
    # version
    v = int(transmision_b[idx + l_idx:idx + l_idx + 3], 2)
    l_idx += 3
    # type
    t = int(transmision_b[idx + l_idx:idx + l_idx + 3], 2)
    l_idx += 3

    # literal
    if t == 4:
        last = False
        n = 0
        i = 0
        while not last:
            last = transmision_b[idx + l_idx] == '0'
            l_idx += 1
            n += 10 ** i * int(transmision_b[idx + l_idx:idx + l_idx + 4], 2)
            l_idx += 4
        return l_idx, op + [n]
    else:
        type_length = transmision_b[idx + l_idx]
        if type_length == '0':
            l_idx += 1
            length = int(transmision_b[idx + l_idx:idx + l_idx + 15], 2)
            processed = 0
            l_idx += 15
            while processed < length:
                p, op = calculate(idx + l_idx, op)
                l_idx += p
                processed += p
            return l_idx, op + [tr(t)]
        else:
            l_idx += 1
            packets = int(transmision_b[idx + l_idx:idx + l_idx + 11], 2)
            l_idx += 11
            processed = 0
            for i in range(packets):
                p, op = calculate(idx + l_idx, op)
                l_idx += p
                processed += p
            return l_idx, op + [tr(t)]


def prn(op):
    stack = []
    n = 0
    for elem in op:
        if type(elem) == int:
            stack.append(elem)
            n += 1
        else:
            pt = []
            if elem == 'sum':
                total = 0
                while n > 0:
                    total += stack.pop()
                    n -= 1
                stack.append(total)
            elif elem == 'mul':
                total = 1
                while n > 0:
                    total *= stack.pop()
                    n -= 1
                stack.append(total)
            elif elem == 'min':
                while n > 0:
                    pt.append(stack.pop())
                    n -= 1
                stack.append(min(pt))
            elif elem == 'max':
                while len(stack) > 0:
                    pt.append(stack.pop())
                stack.append(max(pt))
            elif elem == 'gt':
                if stack.pop() < stack.pop():
                    stack.append(1)
                else:
                    stack.append(0)
            elif elem == 'lt':
                if stack.pop() > stack.pop():
                    stack.append(1)
                else:
                    stack.append(0)
            elif elem == 'eq':
                if stack.pop() == stack.pop():
                    stack.append(1)
                else:
                    stack.append(0)
    return stack[0]


if __name__ == '__main__':
    transmision = read_input('test.txt')
    transmision_b = ''.join([bin(int(x, 16))[2:].zfill(4) for x in transmision])
    # print(transmision_b)
    #
    # version, _ = analize_packet(0, [])
    # print(sum(version))

    _, operations = calculate(0, [])
    print(prn(operations))
