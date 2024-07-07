# python3


# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def printEquisatisfiableSatFormula(n, edges):
    edges_dict = {}
    for item in edges:
        if int(item[0]) < int(item[1]):
            edges_dict[(item[0], item[1])] = 0
        else:
            edges_dict[(item[1], item[0])] = 0

    output_list = []

    # Each vertex belongs to a path
    for v in range(n):
        output_list.append(" ".join([str(n * v + p) for p in range(1, n + 1)]) + " 0")

    # Each vertex appears just once in a path
    for v in range(n):
        for p1 in range(1, n + 1):
            for p2 in range(p1 + 1, n + 1):
                output_list.append(str(-(n * v + p1)) + " " + str(-(n * v + p2)) + " 0")

    # Each position in a path is occupied by some vertex.
    for p in range(1, n + 1):
        output_list.append(" ".join([str(n * v + p) for v in range(n)]) + " 0")

    # No two vertices occupy the same position of a path
    for p in range(1, n + 1):
        for v1 in range(n):
            for v2 in range(v1 + 1, n):
                output_list.append(str(-(n * v1 + p)) + " " + str(-(n * v2 + p)) + " 0")

    # Two successive vertices on a path must be connected by an edge
    for v1 in range(0, n):
        for v2 in range(v1 + 1, n):
            try:
                edges_dict[(v1 + 1, v2 + 1)]
            except:
                for p in range(1, n):
                    output_list.append(
                        str(-(n * v1 + p)) + " " + str(-(n * v2 + p + 1)) + " 0"
                    )
                    output_list.append(
                        str(-(n * v1 + p + 1)) + " " + str(-(n * v2 + p)) + " 0"
                    )

    print(str(len(output_list)) + " " + str(n * n))
    for text in output_list:
        print(text)


if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    printEquisatisfiableSatFormula(n, edges)
