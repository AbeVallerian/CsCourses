# python3
n, m = map(int, input().split())
edges = [list(map(int, input().split())) for i in range(m)]


def printEquisatisfiableSatFormula(n_vertex, edges):
    c = n_vertex * 4 + len(edges) * 3
    v = n_vertex * 3
    print(str(c) + " " + str(v))

    for i in range(n_vertex):
        print(str(3 * i + 1) + " " + str(3 * i + 2) + " " + str(3 * i + 3) + " 0")
        print(str(-(3 * i + 1)) + " " + str(-(3 * i + 2)) + " 0")
        print(str(-(3 * i + 1)) + " " + str(-(3 * i + 3)) + " 0")
        print(str(-(3 * i + 2)) + " " + str(-(3 * i + 3)) + " 0")
    for u, v in edges:
        print(str(-(3 * (u - 1) + 1)) + " " + str(-(3 * (v - 1) + 1)) + " 0")
        print(str(-(3 * (u - 1) + 2)) + " " + str(-(3 * (v - 1) + 2)) + " 0")
        print(str(-(3 * (u - 1) + 3)) + " " + str(-(3 * (v - 1) + 3)) + " 0")


printEquisatisfiableSatFormula(n, edges)
