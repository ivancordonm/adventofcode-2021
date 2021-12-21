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


def calculate(idx, stack):
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
        n = ''
        i = 0
        while not last:
            last = transmision_b[idx + l_idx] == '0'
            l_idx += 1
            n += transmision_b[idx + l_idx:idx + l_idx + 4]
            l_idx += 4
        int_n = int(n, 2)
        return l_idx, stack + [int_n], 1
    else:
        nelem = 0
        type_length = transmision_b[idx + l_idx]
        if type_length == '0':
            l_idx += 1
            length = int(transmision_b[idx + l_idx:idx + l_idx + 15], 2)
            processed = 0
            l_idx += 15
            while processed < length:
                p, stack, n = calculate(idx + l_idx, stack)
                nelem += n
                l_idx += p
                processed += p
            return l_idx, prn(stack, nelem, tr(t)), 1
        else:
            l_idx += 1
            packets = int(transmision_b[idx + l_idx:idx + l_idx + 11], 2)
            l_idx += 11
            processed = 0
            for i in range(packets):
                p, stack, n = calculate(idx + l_idx, stack)
                nelem += n
                l_idx += p
                processed += p
            return l_idx, prn(stack, nelem, tr(t)), 1


def prn(stack, n, type_op):
    pt = []
    if type_op == 'sum':
        total = 0
        for i in range(n):
            total += stack.pop()
        stack.append(total)
    elif type_op == 'mul':
        total = 1
        for i in range(n):
            total *= stack.pop()
        stack.append(total)
    elif type_op == 'min':
        for i in range(n):
            pt.append(stack.pop())
        total = min(pt)
        stack.append(total)
    elif type_op == 'max':
        for i in range(n):
            pt.append(stack.pop())
        total = max(pt)
        stack.append(total)
    elif type_op == 'gt':
        if stack.pop() < stack.pop():
            total = 1
        else:
            total = 0
        stack.append(total)
    elif type_op == 'lt':
        if stack.pop() > stack.pop():
            total = 1
        else:
            total = 0
        stack.append(total)
    elif type_op == 'eq':
        if stack.pop() == stack.pop():
            total = 1
        else:
            total = 0
        stack.append(total)
    return stack


if __name__ == '__main__':
    transmision = read_input('input.txt')
    transmision_b = ''.join([bin(int(x, 16))[2:].zfill(4) for x in transmision])
    # print(transmision_b)
    #
    # version, _ = analize_packet(0, [])
    # print(sum(version))

    _, operations, _ = calculate(0, [])
    print(operations[0])
