from sys import stdin
from typing import Dict, List, Tuple


def check_subset(
    values: List[int], idx: int, w1: int, w2: int, w3: int, lookup: Dict
) -> int:
    if w1 == 0 and w2 == 0 and w3 == 0:
        return 1
    if idx < 0:
        return 0

    key: Tuple = (idx, w1, w2, w3)
    if key not in lookup:
        add1: int = 0
        if w1 >= values[idx]:
            add1 = check_subset(values, idx - 1, w1 - values[idx], w2, w3, lookup)

        add2: int = 0
        if add1 == 0 and w2 >= values[idx]:
            add2 = check_subset(values, idx - 1, w1, w2 - values[idx], w3, lookup)

        add3: int = 0
        if add1 + add2 == 0 and w3 >= values[idx]:
            add3 = check_subset(values, idx - 1, w1, w2, w3 - values[idx], lookup)

        lookup[key] = add1 + add2 + add3

    return lookup[key]


def partition3(values: List[int]) -> int:
    if sum(values) % 3 != 0 or len(values) < 3:
        return 0

    lookup_dict: Dict = {}

    return check_subset(
        values,
        len(values) - 1,
        sum(values) / 3,
        sum(values) / 3,
        sum(values) / 3,
        lookup_dict,
    )


def test_cases() -> None:
    print(partition3([3, 3, 3, 3]) == 0)
    print(partition3([30]) == 0)
    print(partition3([1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25]) == 1)
    print(partition3([3, 6, 4, 1, 9, 6, 9, 1]) == 1)


if __name__ == "__main__":
    input_n, *input_values = list(map(int, stdin.read().split()))
    assert input_n == len(input_values)
    print(partition3(input_values))

    # test_cases()
