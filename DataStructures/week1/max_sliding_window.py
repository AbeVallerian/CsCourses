from collections import deque
from typing import Deque, List


def max_sliding_window_naive(sequence: List[int], m: int) -> List[int]:
    curr_window: Deque[int] = deque([])
    for i in range(m):
        while curr_window and sequence[i] >= sequence[curr_window[-1]]:
            curr_window.pop()
        curr_window.append(i)

    maximums: List[int] = [sequence[curr_window[0]]]
    for i in range(m, len(sequence)):
        while curr_window and curr_window[0] <= i - m:
            curr_window.popleft()
        while curr_window and sequence[i] >= sequence[curr_window[-1]]:
            curr_window.pop()
        curr_window.append(i)
        maximums.append(sequence[curr_window[0]])

    return maximums


def test_cases() -> None:
    print(max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 4) == [7, 7, 5, 6, 6])
    print(
        max_sliding_window_naive([2, 7, 3, 1, 5, 2, 6, 2], 1)
        == [2, 7, 3, 1, 5, 2, 6, 2]
    )
    print(max_sliding_window_naive([0] * 10000, 3333) == [0] * 6668)


if __name__ == "__main__":
    n: int = int(input())
    input_sequence: List[int] = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size: int = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

    # test_cases()
