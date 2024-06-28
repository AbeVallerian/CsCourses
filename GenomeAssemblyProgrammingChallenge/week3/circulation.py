# python3
import copy
from collections import deque
from sys import maxsize


class FlowGraph:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.lb_in = [[] for _ in range(n)]
        self.lb_out = [[] for _ in range(n)]
        self.adj_matrix = [[[0] for _ in range(n)] for _ in range(n)]
        self.visited = [False for _ in range(n)]
        self.parent = [-1 for _ in range(n)]

    def add_edge(self, from_, to, lb, capacity):
        self.graph[from_].append(to)
        self.graph[to].append(from_)
        if self.adj_matrix[from_][to] == [0]:
            self.adj_matrix[from_][to] = [capacity - lb]
        else:
            self.adj_matrix[from_][to].append(capacity - lb)
        if lb > 0:
            self.lb_in[to].append(lb)
            self.lb_out[from_].append(lb)

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
                if not self.visited[v]:
                    if sum(self.adj_matrix[u][v]) > 0:
                        queue.append(v)
                        self.visited[v] = True
                        self.parent[v] = u

        return self.visited[t]


def generate_data(vertex_count, edges):
    graph = FlowGraph(vertex_count + 2)
    for u, v, lb, capacity in edges:
        graph.add_edge(u, v, lb, capacity)
    for u, lb in enumerate(graph.lb_in):
        if u == 0:
            continue
        graph.add_edge(0, u, 0, sum(lb))
    for u, lb in enumerate(graph.lb_out):
        if u == 0 or u == vertex_count + 1:
            continue
        graph.add_edge(u, vertex_count + 1, 0, sum(lb))
    return graph


def max_flow(graph, from_, to):
    flow = 0
    while graph.bfs(from_, to):
        path_flow = maxsize
        s = to
        while s != from_:
            path_flow = min(path_flow, sum(graph.adj_matrix[graph.parent[s]][s]))
            s = graph.parent[s]

        flow += path_flow
        v = to
        while v != from_:
            u = graph.parent[v]

            deduct_flow = path_flow
            for i, f in enumerate(graph.adj_matrix[u][v]):
                if f >= deduct_flow:
                    graph.adj_matrix[u][v][i] -= deduct_flow
                else:
                    graph.adj_matrix[u][v][i] = 0
                    deduct_flow -= f
                if deduct_flow == 0:
                    break

            graph.adj_matrix[v][u][0] += path_flow
            v = graph.parent[v]

    return flow


def check_circulation(graph, max_flow):
    sum_lb = 0
    for lb in graph.lb_in:
        sum_lb += sum(lb)
    return max_flow == sum_lb


def calculate_flow(edges, graph, adj_matrix):
    flows = []
    counter = {}
    for u, v, lb, _ in edges:
        key = str(u) + "_" + str(v)
        if key not in counter.keys():
            flows.append(lb + adj_matrix[u][v][0] - graph.adj_matrix[u][v][0])
            counter[key] = 1
        else:
            flows.append(
                lb
                + adj_matrix[u][v][counter[key]]
                - graph.adj_matrix[u][v][counter[key]]
            )
            counter[key] += 1
    return flows


def test_cases():
    edges = [[1, 2, 0, 3], [2, 3, 0, 3]]
    graph = generate_data(3, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 4)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [0, 0]

    edges = [[1, 2, 0, 3], [1, 2, 0, 3], [2, 3, 0, 3]]
    graph = generate_data(3, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 4)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [0, 0, 0]

    edges = [[1, 2, 1, 3], [2, 3, 2, 4], [3, 1, 1, 2]]
    graph = generate_data(3, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 4)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [2, 2, 2]

    edges = [[1, 2, 1, 3], [2, 3, 2, 3], [2, 3, 0, 1], [3, 1, 1, 2]]
    graph = generate_data(3, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 4)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [2, 2, 0, 2]

    edges = [[1, 2, 1, 3], [2, 3, 2, 4], [1, 3, 1, 2]]
    graph = generate_data(3, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 4)
    assert check_circulation(graph, mx) == False

    edges = [
        [1, 2, 0, 1],
        [1, 3, 0, 1],
        [2, 4, 0, 1],
        [3, 4, 0, 1],
        [2, 5, 0, 1],
        [4, 6, 0, 1],
        [5, 6, 0, 1],
        [6, 1, 2, 2],
    ]
    graph = generate_data(6, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 7)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [1, 1, 0, 1, 1, 1, 1, 2]

    edges = [
        [1, 2, 1, 3],
        [1, 3, 1, 2],
        [2, 3, 1, 5],
        [2, 4, 1, 3],
        [4, 1, 1, 4],
        [3, 4, 1, 3],
    ]
    graph = generate_data(4, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 5)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [2, 1, 1, 1, 3, 2]

    edges = [
        [1, 2, 2, 4],
        [1, 5, 1, 3],
        [1, 3, 2, 5],
        [3, 2, 1, 3],
        [3, 4, 1, 2],
        [5, 4, 1, 4],
        [2, 6, 2, 4],
        [4, 6, 1, 5],
        [5, 6, 2, 5],
        [6, 1, 2, 7],
    ]
    graph = generate_data(6, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, 7)
    assert check_circulation(graph, mx) == True
    assert calculate_flow(edges, graph, adj_matrix) == [2, 3, 2, 1, 1, 1, 3, 2, 2, 7]


def read_data():
    vertex_count, edge_count = map(int, input().split())
    edges = []
    for _ in range(edge_count):
        u, v, lb, capacity = map(int, input().split())
        edges.append([u, v, lb, capacity])
    return vertex_count, edges


if __name__ == "__main__":
    vertex_count, edges = read_data()
    graph = generate_data(vertex_count, edges)
    adj_matrix = copy.deepcopy(graph.adj_matrix)
    mx = max_flow(graph, 0, vertex_count + 1)
    if check_circulation(graph, mx):
        print("YES")
        for f in calculate_flow(edges, graph, adj_matrix):
            print(f)
    else:
        print("NO")

    # test_cases()
