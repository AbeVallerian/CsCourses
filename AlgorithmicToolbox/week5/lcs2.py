from typing import List


def lcs2(first_sequence: List[int], second_sequence: List[int]) -> int:
    max_sequence: List[List[int]] = [
        [0 for j in range(len(second_sequence) + 1)]
        for i in range(len(first_sequence) + 1)
    ]

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                max_sequence[i][j] = 1 + max_sequence[i - 1][j - 1]
            else:
                max_sequence[i][j] = max(max_sequence[i - 1][j], max_sequence[i][j - 1])

    return max_sequence[-1][-1]


def test_cases() -> None:
    print(lcs2([2, 7, 5], [2, 5]) == 2)
    print(lcs2([7], [2, 5]) == 0)
    print(lcs2([2, 7, 8, 3], [5, 2, 8, 7]) == 2)


if __name__ == "__main__":
    n: int = int(input())
    a: List[int] = list(map(int, input().split()))
    assert len(a) == n

    m: int = int(input())
    b: List[int] = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))

    # test_cases()
