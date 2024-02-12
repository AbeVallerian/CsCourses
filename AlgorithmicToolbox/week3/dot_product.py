from typing import List


def max_dot_product(first_sequence: List[int], second_sequence: List[int]) -> int:
    sorted_first_sequence: List[int] = sorted(first_sequence)
    sorted_second_sequence: List[int] = sorted(second_sequence)

    max_product: int = 0
    for i, _ in enumerate(sorted_first_sequence):
        max_product += sorted_first_sequence[i] * sorted_second_sequence[i]

    return max_product


def test_cases() -> None:
    print(max_dot_product([23], [39]) == 897)
    print(max_dot_product([2, 3, 9], [7, 4, 2]) == 79)


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))

    # test_cases()
