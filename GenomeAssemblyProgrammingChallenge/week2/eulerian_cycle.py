# python3
import copy
import sys


def is_eulerian(adj, n):
    in_v = [0 for _ in range(n)]
    out_v = [0 for _ in range(n)]
    for u, vs in enumerate(adj):
        for v in vs:
            out_v[u] += 1
            in_v[v] += 1
    for i in range(n):
        if in_v[i] != out_v[i]:
            return False
    return True


def test_is_eulerian():
    adj = [[1], [1, 2], [0]]
    assert is_eulerian(adj, 3) == True

    adj = [[1, 2], [2], [0]]
    assert is_eulerian(adj, 3) == False


def get_route(adj, route=[]):
    ori_adj = copy.deepcopy(adj)

    if len(route) == 0:
        route.append(0)
    else:
        # retrace
        for i, u in enumerate(route):
            if i == len(route) - 1:
                break
            adj[route[i]].remove(route[i + 1])

    while len(adj[route[-1]]) > 0:
        next_point = adj[route[-1]].pop(0)
        route.append(next_point)
    route = route[:-1]

    for i, u in enumerate(route):
        if len(adj[u]) > 0:
            reroute = route[i:] + route[:i]
            route = get_route(ori_adj, route=reroute)
            break

    return route


def test_get_route():
    adj = [[1], [1, 2], [0]]
    assert get_route(adj) == [0, 1, 1, 2]

    adj = [[1], [1, 2], [0, 2]]
    assert get_route(adj) == [2, 0, 1, 1, 2]

    adj = [[1, 3], [0, 3], [1], [0, 2]]
    assert get_route(adj) == [1, 0, 3, 0, 1, 3, 2]


def read_data():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]

    edges = list(zip(data[0 : (2 * m) : 2], data[1 : (2 * m) : 2]))
    adj = [[] for _ in range(n)]
    for a, b in edges:
        adj[a - 1].append(b - 1)

    return n, adj


if __name__ == "__main__":
    n, adj = read_data()
    if is_eulerian(adj, n):
        print(1)
        route = get_route(adj)
        print(" ".join([str(u + 1) for u in route]))
    else:
        print(0)

    # test_is_eulerian()
    # test_get_route()
