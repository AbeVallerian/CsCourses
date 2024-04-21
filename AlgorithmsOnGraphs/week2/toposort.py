# Uses python3

import sys
from collections import deque


def toposort(adj):
    def dfs(x):
        used[x] = 1
        for w in adj[x]:
            if used[w] == 0:
                dfs(w)
        order.appendleft(x)

    used = [0] * len(adj)
    order = deque([])
    for i in range(len(adj)):
        if used[i] == 0:
            dfs(i)
    return list(order)


def test_cases():
    edges = [[1, 2], [4, 1], [3, 1]]
    adj = [[] for _ in range(4)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(toposort(adj) == [3, 2, 0, 1])

    edges = [[3, 1]]
    adj = [[] for _ in range(4)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(toposort(adj) == [3, 2, 1, 0])

    edges = [[2, 1], [3, 2], [3, 1], [4, 3], [4, 1], [5, 2], [5, 3]]
    adj = [[] for _ in range(5)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(toposort(adj) == [4, 3, 2, 1, 0])


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=" ")

    # test_cases()
