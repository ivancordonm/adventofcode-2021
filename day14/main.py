from collections import Counter


def read_input(filename):
    with open(filename) as f:
        c = [x for x in f.readline().strip()]
        f.readline()
        l = []
        for line in f:
            l.append(line.strip().split(' -> '))
    return c, l


def evolve_chain(c, links_, steps):
    for step in range(steps):
        new_c = []
        for i in (range(len(c) - 1)):
            next_value = [c[i]]
            for link_ in links_:
                if c[i] + c[i + 1] == link_[0]:
                    next_value = [c[i], link_[1]]
                    break
            new_c.extend(next_value)
        c[:] = new_c + [c[-1]]

    return c


def fill_dict(c, links_):
    pairs = {}
    for i in range(len(c) - 1):
        if c[i] + c[i + 1] not in pairs:
            pairs[c[i] + c[i + 1]] = 1
        else:
            pairs[c[i] + c[i + 1]] += 1

    for link in links_:
        if link[0][0] + link[1] not in pairs:
            pairs[link[0][0] + link[1]] = 0
        if link[1] + link[0][1] not in pairs:
            pairs[link[1] + link[0][1]] = 0

    return pairs


def update_pairs(pairs, partial_pairs):
    for p in partial_pairs:
        if p not in pairs.keys():
            pairs[p] = partial_pairs[p]
        else:
            pairs[p] += partial_pairs[p]
    return pairs


def evolve_chain_2(c, links_, steps):
    pairs = fill_dict(c, links_)
    el = Counter([x for x in c])
    for step in range(steps):
        list_pairs_more_1 = [k for k in pairs if pairs[k] > 0]
        partial_pairs = {}
        for pair in list_pairs_more_1:
            for link in links_:
                if pair == link[0]:
                    val = pairs[pair]
                    if link[1] not in el:
                        el[link[1]] = val
                    else:
                        el[link[1]] += val
                    pairs[pair] = 0
                    if link[0][0] + link[1] not in partial_pairs.keys():
                        partial_pairs[link[0][0] + link[1]] = val
                    else:
                        partial_pairs[link[0][0] + link[1]] += val
                    if link[1] + link[0][1] not in partial_pairs.keys():
                        partial_pairs[link[1] + link[0][1]] = val
                    else:
                        partial_pairs[link[1] + link[0][1]] += val
        pairs = update_pairs(pairs, partial_pairs)

    return el


if __name__ == "__main__":
    main_chain, links = read_input("input.txt")
    chain = main_chain.copy()
    chain = evolve_chain(chain, links, 10)
    ccc = Counter(chain)
    max_element = chain.count(max(set(chain), key=chain.count))
    min_element = chain.count(min(set(chain), key=chain.count))
    print("Part 1: ", max_element - min_element)
    print("Part 1: ", max_element, " - ", min_element)
    elements = evolve_chain_2(main_chain, links, 40)
    max_element = max(elements.values())
    min_element = min(elements.values())
    print("Part 2: ", max_element - min_element)
    print("Part 2: ", max_element, " - ", min_element)
