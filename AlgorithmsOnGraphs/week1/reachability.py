# Uses python3

import sys


def find_connection(v, adj, visited, key=None):
    visited[v] = 1
    for w in adj[v]:
        if w == key:
            return 1
        if visited[w] == 0:
            connected = find_connection(w, adj, visited, key=key)
            if connected == 1:
                return 1
    return 0


def reach(adj, x, y):
    visited = {i: 0 for i in range(len(adj))}
    return find_connection(x, adj, visited, key=y)


def test_cases():
    edges = [[1, 2], [3, 2]]
    adj = [[] for _ in range(4)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, 0, 3) == 0)

    edges = [[1, 2], [3, 2], [4, 3], [1, 4]]
    adj = [[] for _ in range(4)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, 0, 3) == 1)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    x, y = data[2 * m :]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for a, b in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

    # test_cases()
