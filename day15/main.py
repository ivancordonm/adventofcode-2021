import heapq as heap
import sys
from collections import defaultdict
from copy import deepcopy


def read_cavern(filename):
    cavern_ = []
    with open(filename) as f:
        for line in f:
            cavern_.append([int(x) for x in line.strip()])
    return cavern_


def calculate_min(cavern_):
    cost_cavern = [[sys.maxsize for _ in range(len(cavern_))] for _ in range(len(cavern_[0]))]
    aux = cavern_[0][0]
    cavern_[0][0] = cost_cavern[0][0] = 0
    for i in range(len(cavern_)):
        for j in range(len(cavern_[i])):
            if j < len(cavern_[0]) - 1:
                cost = cost_cavern[i][j] + cavern_[i][j + 1]
                if cost < cost_cavern[i][j + 1]:
                    cost_cavern[i][j + 1] = cost
            if i < len(cavern_) - 1:
                cost = cost_cavern[i][j] + cavern_[i + 1][j]
                if cost < cost_cavern[i + 1][j]:
                    cost_cavern[i + 1][j] = cost
    cavern_[0][0] = aux
    return cost_cavern[-1][-1]


def neighbors(p, max_i, max_j):
    i, j = p
    neighbor = []
    if i > 0:
        neighbor.append((i - 1, j))
    if j > 0:
        neighbor.append((i, j - 1))
    if i < max_i - 1:
        neighbor.append((i + 1, j))
    if j < max_j - 1:
        neighbor.append((i, j + 1))
    return neighbor


def calculate_min_dijsktra(cavern_, start=(0, 0)):
    visited = set()
    parents = {}
    pq = []
    nodeCosts = defaultdict(lambda: float('inf'))
    nodeCosts[start] = 0
    heap.heappush(pq, (0, start))

    print("Len cavern: ", len(cavern_) * len(cavern_[0]))
    while pq:
        _, current_vertex = heap.heappop(pq)
        visited.add(current_vertex)
        # if len(visited) % 1000 == 0:
        #     print(len(visited))
        for neighbor in neighbors(current_vertex, len(cavern_), len(cavern_[0])):
            distance = cavern_[neighbor[0]][neighbor[1]]
            if neighbor not in visited:
                old_cost = nodeCosts[neighbor]
                new_cost = nodeCosts[current_vertex] + distance
                if new_cost < old_cost:
                    parents[neighbor] = current_vertex
                    nodeCosts[neighbor] = new_cost
                    heap.heappush(pq, (new_cost, neighbor))

    return nodeCosts, parents


def concat_h(h_cavern, p_cavern):
    if len(h_cavern) == 0:
        return p_cavern
    else:
        for i in range(len(h_cavern)):
            for j in range(len(p_cavern[i])):
                h_cavern[i].append(p_cavern[i][j])
        return h_cavern


def concat_v(fcavern, h_cavern):
    if len(fcavern) == 0:
        return h_cavern
    else:
        for i in range(len(h_cavern)):
            fcavern.append(h_cavern[i])
        return fcavern


def get_full_cavern(cavern_, s):
    fcavern = []
    if s == 1:
        return cavern_
    else:
        list_cavern = [cavern_]
        cavern_aux = deepcopy(cavern_)
        for m in range(s + s - 2):
            for i in range(len(cavern_aux)):
                for j in range(len(cavern_aux[i])):
                    if cavern_aux[i][j] < 9:
                        cavern_aux[i][j] = cavern_aux[i][j] + 1
                    else:
                        cavern_aux[i][j] = 1
            list_cavern.append(deepcopy(cavern_aux))
        for i in range(s):
            h_cavern = []
            for j in range(s):
                h_cavern = concat_h(h_cavern, list_cavern[i + j])
            fcavern = concat_v(fcavern, h_cavern)

        return fcavern


if __name__ == '__main__':
    cavern = read_cavern("input.txt")
    d, p = calculate_min_dijsktra(cavern)
    print("Minimum cost is", d[(len(cavern) - 1, len(cavern[0]) - 1)])

    # goal = (len(cavern) - 1, len(cavern[0]) - 1)
    # min = calculate_min(cavern)
    # print(min)

    full_cavern = get_full_cavern(cavern, 5)
    d, p = calculate_min_dijsktra(full_cavern)
    print("Minimum cost is", d[(len(cavern) - 1, len(cavern[0]) - 1)])
