import sys
import threading
from typing import Dict, List

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**28)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n: int = int(sys.stdin.readline())
        self.key: Dict[int, int] = {}
        self.left: Dict[int, int] = {}
        self.right: Dict[int, int] = {}
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, root_idx: int = 0) -> None:
        left: int = self.left[root_idx]
        right: int = self.right[root_idx]
        key: int = self.key[root_idx]

        if left != -1:
            self.inOrder(left)
        print(key, end=" ")
        if right != -1:
            self.inOrder(right)
        # if left == -1 and right == -1:
        #     return [key]
        # elif left == -1:
        #     return [key] + self.inOrder(right)
        # elif right == -1:
        #     return self.inOrder(left) + [key]
        # return self.inOrder(left) + [key] + self.inOrder(right)

    def preOrder(self, root_idx: int = 0) -> None:
        left: int = self.left[root_idx]
        right: int = self.right[root_idx]
        key: int = self.key[root_idx]

        print(key, end=" ")
        if left != -1:
            self.preOrder(left)
        if right != -1:
            self.preOrder(right)

        # if left == -1 and right == -1:
        #     return [key]
        # elif left == -1:
        #     return [key] + self.preOrder(right)
        # elif right == -1:
        #     return [key] + self.preOrder(left)
        # return [key] + self.preOrder(left) + self.preOrder(right)

    def postOrder(self, root_idx: int = 0) -> None:
        left: int = self.left[root_idx]
        right: int = self.right[root_idx]
        key: int = self.key[root_idx]

        if left != -1:
            self.postOrder(left)
        if right != -1:
            self.postOrder(right)
        print(key, end=" ")

        # if left == -1 and right == -1:
        #     return [key]
        # elif left == -1:
        #     return self.postOrder(right) + [key]
        # elif right == -1:
        #     return self.postOrder(left) + [key]
        # return self.postOrder(left) + self.postOrder(right) + [key]


def main() -> None:
    tree: TreeOrders = TreeOrders()
    tree.read()
    # print(" ".join(str(x) for x in tree.inOrder()))
    # print(" ".join(str(x) for x in tree.preOrder()))
    # print(" ".join(str(x) for x in tree.postOrder()))

    tree.inOrder()
    print()
    tree.preOrder()
    print()
    tree.postOrder()


threading.Thread(target=main).start()
