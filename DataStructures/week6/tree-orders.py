import sys
import threading
from typing import List

sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n: int = int(sys.stdin.readline())
        self.key: List[int] = [0 for _ in range(self.n)]
        self.left: List[int] = [0 for _ in range(self.n)]
        self.right: List[int] = [0 for _ in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, root_idx: int = 0) -> List[int]:
        if self.right[root_idx] == -1 and self.right[root_idx] == -1:
            return [self.key[root_idx]]
        elif self.left[root_idx] == -1:
            return [self.key[root_idx]] + self.inOrder(self.right[root_idx])
        elif self.right[root_idx] == -1:
            return self.inOrder(self.left[root_idx]) + [self.key[root_idx]]
        return (
            self.inOrder(self.left[root_idx])
            + [self.key[root_idx]]
            + self.inOrder(self.right[root_idx])
        )

    def preOrder(self, root_idx: int = 0) -> List[int]:
        if self.left[root_idx] == -1 and self.right[root_idx] == -1:
            return [self.key[root_idx]]
        elif self.left[root_idx] == -1:
            return [self.key[root_idx]] + self.preOrder(self.right[root_idx])
        elif self.right[root_idx] == -1:
            return [self.key[root_idx]] + self.preOrder(self.left[root_idx])
        return (
            [self.key[root_idx]]
            + self.preOrder(self.left[root_idx])
            + self.preOrder(self.right[root_idx])
        )

    def postOrder(self, root_idx: int = 0) -> List[int]:
        if self.left[root_idx] == -1 and self.right[root_idx] == -1:
            return [self.key[root_idx]]
        elif self.left[root_idx] == -1:
            return self.postOrder(self.right[root_idx]) + [self.key[root_idx]]
        elif self.right[root_idx] == -1:
            return self.postOrder(self.left[root_idx]) + [self.key[root_idx]]
        return (
            self.postOrder(self.left[root_idx])
            + self.postOrder(self.right[root_idx])
            + [self.key[root_idx]]
        )


def main() -> None:
    tree: TreeOrders = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
