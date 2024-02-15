import sys
import threading
from typing import Dict, List


def get_tree_height(children: List[int], tree: Dict) -> int:
    if len(children) == 0:
        return 1
    else:
        heights: List[int] = []
        for child in children:
            heights.append(1 + get_tree_height(tree[child]["child"], tree))
        return max(heights)


def compute_height(n: int, parents: List[int]) -> int:
    tree: Dict = {}
    for i in range(n):
        tree[i] = {"parent": -1, "child": []}

    max_height: int = 0
    root: int = -1
    for i, parent in enumerate(parents):
        if parent != -1:
            tree[i]["parent"] = parent
            tree[parent]["child"].append(i)
        else:
            root = i

    return get_tree_height(tree[root]["child"], tree)


def test_cases() -> None:
    print(compute_height(1, [-1]) == 1)
    print(compute_height(5, [4, -1, 4, 1, 1]) == 3)
    print(compute_height(3, [1, -1, 1]) == 2)
    print(compute_height(5, [-1, 0, 4, 0, 3]) == 4)


def main() -> None:
    n: int = int(input())
    parents: List[int] = list(map(int, input().split()))
    print(compute_height(n, parents))

    # test_cases()


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
threading.Thread(target=main).start()
