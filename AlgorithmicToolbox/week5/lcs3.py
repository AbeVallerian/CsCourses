from typing import List


def lcs3(
    first_sequence: List[int], second_sequence: List[int], third_sequence: List[int]
) -> int:
    max_sequence: List[List[int]] = [
        [
            [0 for _ in range(len(third_sequence) + 1)]
            for _ in range(len(second_sequence) + 1)
        ]
        for _ in range(len(first_sequence) + 1)
    ]

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            for k in range(1, len(third_sequence) + 1):
                if (
                    first_sequence[i - 1] == second_sequence[j - 1]
                    and second_sequence[j - 1] == third_sequence[k - 1]
                ):
                    max_sequence[i][j][k] = 1 + max_sequence[i - 1][j - 1][k - 1]
                else:
                    max_sequence[i][j][k] = max(
                        max_sequence[i - 1][j][k],
                        max_sequence[i][j - 1][k],
                        max_sequence[i][j][k - 1],
                    )

    return max_sequence[-1][-1][-1]


def test_cases() -> None:
    print(lcs3([1, 2, 3], [2, 1, 3], [1, 3, 5]) == 2)
    print(lcs3([8, 3, 2, 1, 7], [8, 2, 1, 3, 8, 10, 7], [6, 8, 3, 1, 4, 7]) == 3)
    print(lcs3([1, 2, 3], [2, 3, 1], [3, 1, 2]) == 1)


if __name__ == "__main__":
    n: int = int(input())
    a: List[int] = list(map(int, input().split()))
    assert len(a) == n

    m: int = int(input())
    b: List[int] = list(map(int, input().split()))
    assert len(b) == m

    q: int = int(input())
    c: List[int] = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))

    # test_cases()
