from sys import stdin
from typing import List


def maximum_gold(capacity: int, weights: List[int]) -> int:
    max_weights: List[List[int]] = [
        [0 for j in range(capacity + 1)] for i in range(len(weights) + 1)
    ]

    for i in range(1, len(weights) + 1):
        for j in range(1, capacity + 1):
            if j >= weights[i - 1]:
                max_weights[i][j] = max(
                    max_weights[i - 1][j],
                    weights[i - 1] + max_weights[i - 1][j - weights[i - 1]],
                )
            else:
                max_weights[i][j] = max_weights[i - 1][j]

    return max_weights[len(weights)][capacity]


def test_cases() -> None:
    print(maximum_gold(10, [1, 4, 8]) == 9)
    print(maximum_gold(20, [4, 5, 5, 6, 6, 6, 8, 8, 9, 9, 10]) == 20)


if __name__ == "__main__":
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))

    # test_cases()
