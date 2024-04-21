# python3
from collections import deque
from sys import maxsize


class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        self.n_flight = n
        self.n_crew = m
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(" ".join(line))

    def bpm(self, u):
        for v in range(self.n_crew):
            if self.graph[u][v] == 1 and self.visited[v] == False:
                self.visited[v] = True
                if self.matching[v] == -1 or self.bpm(self.matching[v]):
                    self.matching[v] = u
                    return True
        return False

    def find_matching(self):
        self.matching = [-1] * self.n_crew

        for i in range(self.n_flight):
            self.visited = [False] * self.n_crew
            self.bpm(i)

        result = [-1] * self.n_flight
        for crew, flight in enumerate(self.matching):
            if flight != -1:
                result[flight] = crew
        return result

    def solve(self, adj_matrix=None):
        if adj_matrix is None:
            adj_matrix = self.read_data()
        else:
            self.n_flight = len(adj_matrix)
            self.n_crew = len(adj_matrix[0])
        self.graph = adj_matrix
        self.matching = [-1] * self.n_crew
        self.visited = [False] * self.n_crew

        matching = self.find_matching()
        self.write_response(matching)

        # return matching


def test_cases():
    adj_matrix = [[1, 1], [1, 0]]
    print(MaxMatching().solve(adj_matrix) == [1, 0])

    adj_matrix = [[1, 1, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0]]
    print(MaxMatching().solve(adj_matrix) == [0, 1, -1])


if __name__ == "__main__":
    max_matching = MaxMatching()
    max_matching.solve()

    # test_cases()
