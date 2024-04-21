# Uses python3

import sys
import queue


def distance(adj, cost, s, t):
    dist = [sys.maxsize for _ in range(len(adj))]
    prev = [-1 for _ in range(len(adj))]
    dist[s] = 0
    prev[s] = s
    qq = queue.PriorityQueue()
    qq.put((0, s))

    while not qq.empty():
        _, u = qq.get()
        for i, v in enumerate(adj[u]):
            if dist[v] > dist[u] + cost[u][i]:
                dist[v] = dist[u] + cost[u][i]
                prev[v] = u
                qq.put((dist[v], v))
    return dist[t] if prev[t] != -1 else -1


def test_cases():
    edges = [((1, 2), 1), ((4, 1), 2), ((2, 3), 2), ((1, 3), 5)]
    adj = [[] for _ in range(4)]
    cost = [[] for _ in range(4)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(distance(adj, cost, 0, 2) == 3)

    edges = [
        ((1, 2), 4),
        ((1, 3), 2),
        ((2, 3), 2),
        ((3, 2), 1),
        ((2, 4), 2),
        ((3, 5), 4),
        ((5, 4), 1),
        ((2, 5), 3),
        ((3, 4), 4),
    ]
    adj = [[] for _ in range(5)]
    cost = [[] for _ in range(5)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(distance(adj, cost, 0, 4) == 6)

    edges = [((1, 2), 7), ((1, 3), 5), ((2, 3), 2)]
    adj = [[] for _ in range(4)]
    cost = [[] for _ in range(4)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(distance(adj, cost, 2, 1) == -1)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0 : (3 * m) : 3], data[1 : (3 * m) : 3]), data[2 : (3 * m) : 3])
    )
    data = data[3 * m :]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))

    # test_cases()
