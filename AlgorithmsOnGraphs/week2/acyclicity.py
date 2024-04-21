# Uses python3

import sys


def acyclic(adj):
    def check_cycle(node):
        if in_stack[node] == True:
            return 1
        if visited[node] == True:
            return 0

        visited[node] = True
        in_stack[node] = True

        for v in adj[node]:
            # Recurse for 'v'.
            if check_cycle(v) == True:
                return 1

        # Mark 'node' to be removed
        # from the recursive stack.
        in_stack[node] = False
        return 0

    visited = [False for i in range(len(adj))]
    in_stack = [False for i in range(len(adj))]
    for i in range(len(adj)):
        if visited[i] == False:
            if check_cycle(i) == 1:
                return 1
    return 0


def test_cases():
    edges = [[1, 2], [4, 1], [2, 3], [3, 1]]
    adj = [[] for _ in range(4)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj) == 1)

    edges = [[1, 2], [2, 3], [1, 3], [3, 4], [1, 4], [2, 5], [3, 5]]
    adj = [[] for _ in range(5)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj) == 0)


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

    # test_cases()
