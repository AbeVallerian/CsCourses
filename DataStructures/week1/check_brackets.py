from collections import namedtuple
from typing import List

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left: str, right: str) -> bool:
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> int:
    opening_brackets_stack: List[str] = []
    opening_brackets_pos: List[int] = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            opening_brackets_pos.append(i + 1)

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i + 1
            elif are_matching(opening_brackets_stack[-1], next):
                opening_brackets_stack.pop()
                opening_brackets_pos.pop()
            else:
                return i + 1
    if len(opening_brackets_stack) > 0:
        return opening_brackets_pos[0]
    return 0


def test_cases() -> None:
    print(find_mismatch("}") == 1)
    print(find_mismatch("[]") == 0)
    print(find_mismatch("{}[]") == 0)
    print(find_mismatch("[()]") == 0)
    print(find_mismatch("(())") == 0)
    print(find_mismatch("{[]}()") == 0)
    print(find_mismatch("{") == 1)
    print(find_mismatch("{[}") == 3)
    print(find_mismatch("foo(bar);") == 0)
    print(find_mismatch("foo(bar[i);") == 10)
    print(find_mismatch("[](()") == 3)


def main():
    text: str = input()
    mismatch: int = find_mismatch(text)
    if mismatch == 0:
        print("Success")
    else:
        print(mismatch)

    # test_cases()


if __name__ == "__main__":
    main()
