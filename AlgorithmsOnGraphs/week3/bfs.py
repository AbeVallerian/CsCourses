# Uses python3

import sys
import queue


def distance(adj, s, t):
    dist = [-1 for i in range(len(adj))]
    dist[s] = 0
    qq = queue.Queue()
    qq.put(s)
    while not qq.empty():
        u = qq.get()
        if u == t:
            break
        for v in adj[u]:
            if dist[v] == -1:
                qq.put(v)
                dist[v] = dist[u] + 1
    return dist[t]


def test_cases():
    edges = [(1, 2), (4, 1), (2, 3), (3, 1)]
    adj = [[] for _ in range(4)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(distance(adj, 1, 3) == 2)

    edges = [(5, 2), (1, 3), (3, 4), (1, 4)]
    adj = [[] for _ in range(5)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(distance(adj, 2, 4) == -1)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))

    # test_cases()
