import sys
import threading
from typing import List, Tuple

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


def IsBinarySearchTree(
    tree: List[Tuple[int, int, int]],
    root_idx: int = 0,
    left_range: int = None,
    right_range: int = None,
) -> bool:
    if len(tree) == 0 or root_idx == -1:
        return True

    key, left_idx, right_idx = tree[root_idx]
    left_key, _, _ = tree[left_idx]
    right_key, _, _ = tree[right_idx]

    if left_idx != -1:
        if left_key >= key:
            return False
        if left_range is not None and left_range > left_key:
            return False
        if right_range is not None and right_range <= left_key:
            return False

    if right_idx != -1:
        if right_key < key:
            return False
        if left_range is not None and left_range > right_key:
            return False
        if right_range is not None and right_range <= right_key:
            return False

    return IsBinarySearchTree(
        tree, left_idx, left_range=left_range, right_range=key
    ) and IsBinarySearchTree(tree, right_idx, left_range=key, right_range=right_range)


def test_cases() -> None:
    print(IsBinarySearchTree([(2, 1, 2), (1, -1, -1), (3, -1, -1)]) == True)
    print(IsBinarySearchTree([(1, 1, 2), (2, -1, -1), (3, -1, -1)]) == False)
    print(IsBinarySearchTree([]) == True)
    print(
        IsBinarySearchTree(
            [(1, -1, 1), (2, -1, 2), (3, -1, 3), (4, -1, 4), (5, -1, -1)]
        )
        == True
    )
    print(
        IsBinarySearchTree([(4, 1, -1), (2, 2, 3), (1, -1, -1), (5, -1, -1)]) == False
    )
    print(IsBinarySearchTree([(2, 1, 2), (1, -1, -1), (2, -1, -1)]) == True)
    print(IsBinarySearchTree([(2, 1, 2), (2, -1, -1), (3, -1, -1)]) == False)
    print(IsBinarySearchTree([(2147483647, -1, -1)]) == True)


def main() -> None:
    nodes: int = int(sys.stdin.readline().strip())
    tree: List[Tuple[int, int, int]] = []
    for _ in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()

# test_cases()
