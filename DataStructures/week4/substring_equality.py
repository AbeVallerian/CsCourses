import sys
from typing import List


class Solver:
    def __init__(
        self,
        s: str,
        multiplier: int = 263,
        m1: int = 1000000007,
    ) -> None:
        self.s: str = s
        self.multiplier: int = multiplier
        self.m1: int = m1

        self.hashed1: List = [0]
        for i in range(1, len(self.s) + 1):
            self.hashed1.append(
                (self.hashed1[i - 1] * self.multiplier + ord(s[i - 1])) % self.m1
            )

    def ask(self, a: int, b: int, l: int) -> bool:
        if a == b:
            return True

        y1: int = 1
        for _ in range(l):
            y1 = (y1 * self.multiplier) % self.m1

        h1_a: int = (
            (self.hashed1[a + l] - y1 * self.hashed1[a]) % self.m1 + self.m1
        ) % self.m1
        h1_b: int = (
            (self.hashed1[b + l] - y1 * self.hashed1[b]) % self.m1 + self.m1
        ) % self.m1

        if h1_a == h1_b:
            return True
        else:
            return False


def test_cases() -> None:
    solver: Solver = Solver("trololo")
    print(solver.ask(0, 0, 7) == True)
    print(solver.ask(2, 4, 3) == True)
    print(solver.ask(3, 5, 1) == True)
    print(solver.ask(1, 3, 2) == False)


if __name__ == "__main__":
    s: str = sys.stdin.readline()
    q: int = int(sys.stdin.readline())
    solver: Solver = Solver(s)
    for i in range(q):
        a, b, l = map(int, sys.stdin.readline().split())
        print("Yes" if solver.ask(a, b, l) else "No")

    # test_cases()
