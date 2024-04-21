# python3
from collections import deque
from sys import maxsize


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n):
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.adj_matrix = [[0] * n for _ in range(n)]
        self.visited = [False for _ in range(n)]
        self.parent = [-1 for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        self.graph[from_].append(to)
        self.graph[to].append(from_)
        self.adj_matrix[from_][to] += capacity

    def size(self):
        return len(self.graph)

    def bfs(self, s, t):
        self.visited = [False for _ in range(self.size())]
        self.visited[s] = True
        queue = deque()
        queue.append(s)

        while len(queue) > 0:
            u = queue.popleft()
            for v in self.graph[u]:
                if not self.visited[v] and self.adj_matrix[u][v] > 0:
                    queue.append(v)
                    self.visited[v] = True
                    self.parent[v] = u

        return self.visited[t]


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def generate_data(vertex_count, edges):
    graph = FlowGraph(vertex_count)
    for u, v, capacity in edges:
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def max_flow(graph, from_, to):
    flow = 0
    while graph.bfs(from_, to):
        path_flow = maxsize
        s = to
        while s != from_:
            path_flow = min(path_flow, graph.adj_matrix[graph.parent[s]][s])
            s = graph.parent[s]

        flow += path_flow
        v = to
        while v != from_:
            u = graph.parent[v]
            graph.adj_matrix[u][v] -= path_flow
            graph.adj_matrix[v][u] += path_flow
            v = graph.parent[v]

    return flow


def test_bfs():
    graph = generate_data(
        5, [[1, 2, 2], [2, 5, 5], [1, 3, 6], [3, 4, 2], [4, 5, 1], [3, 2, 3], [2, 4, 1]]
    )
    print(graph.bfs(0, 0) == True)
    print(graph.bfs(0, 1) == True)
    print(graph.bfs(0, 4) == True)
    print(graph.bfs(2, 0) == False)
    print(graph.bfs(4, 1) == False)


def test_max_flow():
    graph = generate_data(
        5, [[1, 2, 2], [2, 5, 5], [1, 3, 6], [3, 4, 2], [4, 5, 1], [3, 2, 3], [2, 4, 1]]
    )
    print(max_flow(graph, 0, 4) == 6)

    graph = generate_data(
        5, [[1, 2, 2], [2, 5, 5], [1, 3, 6], [3, 4, 2], [4, 5, 1], [3, 2, 3], [2, 4, 1]]
    )
    print(max_flow(graph, 0, 1) == 5)

    graph = generate_data(
        4, [[1, 2, 10000], [1, 3, 10000], [2, 3, 1], [3, 4, 10000], [2, 4, 10000]]
    )
    print(max_flow(graph, 0, 3) == 20000)

    graph = generate_data(
        4, [[1, 2, 10000], [1, 3, 10000], [2, 3, 1], [3, 4, 10000], [2, 4, 10000]]
    )
    print(max_flow(graph, 0, 2) == 10001)


if __name__ == "__main__":
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))

    # test_bfs()
    # test_max_flow()
