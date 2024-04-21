from sys import stdin
from typing import Tuple


# Vertex of a splay tree
class Vertex:
    def __init__(self, key: int, sum: int, left, right, parent) -> None:
        (self.key, self.sum, self.left, self.right, self.parent) = (
            key,
            sum,
            left,
            right,
            parent,
        )


def update(v: Vertex) -> None:
    if v == None:
        return
    v.sum = (
        v.key
        + (v.left.sum if v.left != None else 0)
        + (v.right.sum if v.right != None else 0)
    )
    if v.left != None:
        v.left.parent = v
    if v.right != None:
        v.right.parent = v


def smallRotation(v: Vertex) -> None:
    parent: int = v.parent
    if parent == None:
        return
    grandparent: int = v.parent.parent
    if parent.left == v:
        m = v.right
        v.right = parent
        parent.left = m
    else:
        m = v.left
        v.left = parent
        parent.right = m
    update(parent)
    update(v)
    v.parent = grandparent
    if grandparent != None:
        if grandparent.left == parent:
            grandparent.left = v
        else:
            grandparent.right = v


def bigRotation(v) -> None:
    if v.parent.left == v and v.parent.parent.left == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    elif v.parent.right == v and v.parent.parent.right == v.parent:
        # Zig-zig
        smallRotation(v.parent)
        smallRotation(v)
    else:
        # Zig-zag
        smallRotation(v)
        smallRotation(v)


# Makes splay of the given vertex and makes
# it the new root.
def splay(v: Vertex) -> Vertex:
    if v == None:
        return None
    while v.parent != None:
        if v.parent.parent == None:
            smallRotation(v)
            break
        bigRotation(v)
    return v


# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root: Vertex, key: int) -> Tuple[Vertex, Vertex]:
    v: Vertex = root
    last: Vertex = root
    next: Vertex = None
    while v != None:
        if v.key >= key and (next == None or v.key < next.key):
            next = v
        last = v
        if v.key == key:
            break
        if v.key < key:
            v = v.right
        else:
            v = v.left
    root = splay(last)
    return (next, root)


def split(root: Vertex, key: int) -> Tuple[Vertex, Vertex]:
    (result, root) = find(root, key)
    if result == None:
        return (root, None)
    right: Vertex = splay(result)
    left: Vertex = right.left
    right.left = None
    if left != None:
        left.parent = None
    update(left)
    update(right)
    return (left, right)


def merge(left: Vertex, right: Vertex) -> Vertex:
    if left == None:
        return right
    if right == None:
        return left
    while right.left != None:
        right = right.left
    right = splay(right)
    right.left = left
    update(right)
    return right


# Code that uses splay tree to solve the problem

root: Vertex = None


def insert(x: int) -> None:
    global root
    (left, right) = split(root, x)
    new_vertex: Vertex = None
    if right == None or right.key != x:
        new_vertex = Vertex(x, x, None, None, None)
    root = merge(merge(left, new_vertex), right)
    update(root)


def search(x: int) -> bool:
    global root
    (_, root) = find(root, x)
    if root != None and root.key == x:
        return True
    return False


def erase(x: int) -> None:
    global root
    (result, root) = find(root, x)
    if result == None:
        return
    root = merge(root.left, root.right)
    update(root)


def sum(fr: int, to: int) -> int:
    global root
    (left, middle) = split(root, fr)
    (middle, right) = split(middle, to + 1)
    if middle == None:
        return 0
    return middle.sum


MODULO: int = 1000000001
n: int = int(stdin.readline())
last_sum_result: int = 0
for i in range(n):
    line: str = stdin.readline().split()
    if line[0] == "+":
        x: int = int(line[1])
        insert((x + last_sum_result) % MODULO)
    elif line[0] == "-":
        x: int = int(line[1])
        erase((x + last_sum_result) % MODULO)
    elif line[0] == "?":
        x: int = int(line[1])
        print("Found" if search((x + last_sum_result) % MODULO) else "Not found")
    elif line[0] == "s":
        l: int = int(line[1])
        r: int = int(line[2])
        res: int = sum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
        print(res)
        last_sum_result = res % MODULO
    print("root", root.key)
