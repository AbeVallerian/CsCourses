# uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.links = []
        self.children = []
        self.parent = -2
        self.value = -1


class Tree:
    def __init__(self, vertices):
        self.vertices = vertices

    def dfs(self, vertex, parent):
        self.vertices[vertex].parent = parent
        for child in self.vertices[vertex].links:
            if child != parent:
                self.vertices[vertex].children.append(child)
                self.dfs(child, vertex)

    def calculate_fun(self, vertex):
        if self.vertices[vertex].value == -1:
            m1 = self.vertices[vertex].weight
            for child in self.vertices[vertex].children:
                for g_child in self.vertices[child].children:
                    m1 += self.calculate_fun(g_child)

            m2 = 0
            for child in self.vertices[vertex].children:
                m2 += self.calculate_fun(child)

            self.vertices[vertex].value = max(m1, m2)

        return self.vertices[vertex].value


def generate_vertices(fun_factors, edges):
    vertices = [Vertex(w) for w in fun_factors]
    for edge in edges:
        vertices[edge[1] - 1].links.append(edge[0] - 1)
        vertices[edge[0] - 1].links.append(edge[1] - 1)
    return vertices


def ReadTree():
    size = int(input())
    vertices = [Vertex(w) for w in map(int, input().split())]
    for _ in range(1, size):
        a, b = list(map(int, input().split()))
        vertices[a - 1].links.append(b - 1)
        vertices[b - 1].links.append(a - 1)
    return vertices


def MaxWeightIndependentTreeSubset(vertices):
    size = len(vertices)
    if size == 0:
        return 0

    root = -1
    for i in range(size):
        if len(vertices[i].links) == 1:
            root = i
            break

    tree = Tree(vertices)
    tree.dfs(root, -1)

    fun = tree.calculate_fun(root)

    return fun


def test_cases():
    vertices = generate_vertices([1000], [])
    assert MaxWeightIndependentTreeSubset(vertices) == 1000

    vertices = generate_vertices([1, 2], [[1, 2]])
    assert MaxWeightIndependentTreeSubset(vertices) == 2

    vertices = generate_vertices([1, 5, 3, 7, 5], [[5, 4], [2, 3], [4, 2], [1, 2]])
    assert MaxWeightIndependentTreeSubset(vertices) == 11

    vertices = generate_vertices([1, 1, 1], [[1, 2], [3, 2]])
    assert MaxWeightIndependentTreeSubset(vertices) == 2

    edges = [
        [2, 3],
        [1, 3],
        [4, 3],
        [5, 2],
        [6, 1],
        [7, 4],
        [8, 4],
        [9, 7],
        [10, 7],
        [11, 7],
    ]
    vertices = generate_vertices([3, 5, 1, 6, 2, 3, 7, 2, 1, 2, 1], edges)
    assert MaxWeightIndependentTreeSubset(vertices) == 18

    vertices = generate_vertices([1, 8, 1, 2, 10], [[1, 2], [1, 3], [2, 4], [3, 5]])
    assert MaxWeightIndependentTreeSubset(vertices) == 18


def main():
    vertices = ReadTree()
    weight = MaxWeightIndependentTreeSubset(vertices)
    print(weight)


# This is to avoid stack overflow issues
threading.Thread(target=main).start()

# test_cases()
