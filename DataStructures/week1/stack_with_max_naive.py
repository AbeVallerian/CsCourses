import sys
from typing import List


class StackWithMax:
    def __init__(self):
        self.__stack: List[int] = []
        self.__max_stack: List[int] = []

    def Push(self, a: int) -> None:
        self.__stack.append(a)
        if len(self.__max_stack) == 0:
            self.__max_stack.append(a)
        elif self.__max_stack[-1] >= a:
            self.__max_stack.append(self.__max_stack[-1])
        else:
            self.__max_stack.append(a)

    def Pop(self) -> None:
        assert len(self.__stack)
        self.__stack.pop()
        self.__max_stack.pop()

    def Max(self) -> int:
        assert len(self.__stack)
        return self.__max_stack[-1]


if __name__ == "__main__":
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert 0
