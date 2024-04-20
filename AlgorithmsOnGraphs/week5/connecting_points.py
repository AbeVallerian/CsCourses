# Uses python3
import sys
import math


def get_parent(node, parent):
    if parent[node] == node:
        return node
    else:
        return get_parent(parent[node], parent)


def merge(node1, node2, parent, rank):
    node1_parent = get_parent(node1, parent)
    node2_parent = get_parent(node2, parent)

    if rank[node1_parent] > rank[node2_parent]:
        parent[node2_parent] = node1_parent
    elif rank[node1_parent] == rank[node2_parent]:
        parent[node2_parent] = node1_parent
        rank[node1_parent] += 1
    else:
        parent[node1_parent] = node2_parent

    return parent, rank


def minimum_distance(x, y):
    parent = [i for i in range(len(x))]
    rank = [0 for _ in range(len(x))]

    edges = []
    for i in range(len(x)):
        for j in range(len(y)):
            if i != j:
                edges.append(
                    [
                        i,
                        j,
                        math.sqrt(
                            (x[i] - x[j]) * (x[i] - x[j])
                            + (y[i] - y[j]) * (y[i] - y[j])
                        ),
                    ]
                )
    edges = sorted(edges, key=lambda x: x[-1])

    count_edge = 0
    result = 0.0
    for u, v, dist in edges:
        if get_parent(u, parent) != get_parent(v, parent):
            result += dist
            parent, rank = merge(u, v, parent, rank)
            count_edge += 1
        if count_edge == len(x) - 1:
            break

    return round(result, 7)


def test_cases():
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    print(minimum_distance(x, y) == 3.0)

    x = [0, 0, 1, 3, 3]
    y = [0, 2, 1, 0, 2]
    print(minimum_distance(x, y) == round(7.064495102, 7))


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

    # test_cases()
