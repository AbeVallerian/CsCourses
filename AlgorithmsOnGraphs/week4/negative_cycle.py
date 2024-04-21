# Uses python3

import sys


def negative_cycle(adj, cost):
    dist = [sys.maxsize for _ in range(len(adj))]
    dist[0] = 0
    prev = [-1 for _ in range(len(adj))]

    for step in range(len(adj)):
        if step == len(adj) - 1:
            prev_dist = dist.copy()
        for u in range(len(adj)):
            curr_cost = cost[u]
            for i, v in enumerate(adj[u]):
                if dist[v] > dist[u] + curr_cost[i]:
                    dist[v] = dist[u] + curr_cost[i]
                    prev[v] = u

    return 1 if prev_dist != dist else 0


def test_cases():
    edges = [((1, 2), -5), ((4, 1), 2), ((2, 3), 2), ((3, 1), 1)]
    adj = [[] for _ in range(4)]
    cost = [[] for _ in range(4)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost) == 1)

    edges = [((1, 2), 1), ((4, 1), 2), ((2, 3), 2), ((1, 3), 5)]
    adj = [[] for _ in range(4)]
    cost = [[] for _ in range(4)]
    for (a, b), w in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost) == 0)


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
    print(negative_cycle(adj, cost))

    # test_cases()
