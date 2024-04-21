from typing import List, Tuple


def get_parent(i: int) -> int:
    return i // 2


def get_left_child(i: int) -> int:
    return 2 * i


def get_right_child(i: int) -> int:
    return 2 * i + 1


def build_heap(data: List[int]) -> List[Tuple[int, int]]:
    """Build a heap from ``data`` inplace.
    Returns a sequence of swaps performed by the algorithm.
    """

    def _shif_down(i: int) -> None:
        min_idx: int = i
        if (
            get_left_child(i) <= len(data)
            and data[get_left_child(i) - 1] < data[min_idx - 1]
        ):
            min_idx = get_left_child(i)
        if (
            get_right_child(i) <= len(data)
            and data[get_right_child(i) - 1] < data[min_idx - 1]
        ):
            min_idx = get_right_child(i)
        if i != min_idx:
            swaps.append((min(i - 1, min_idx - 1), max(i - 1, min_idx - 1)))
            data[i - 1], data[min_idx - 1] = data[min_idx - 1], data[i - 1]
            _shif_down(min_idx)

    swaps: List[Tuple[int, int]] = []
    for i in range(len(data) // 2, 0, -1):
        _shif_down(i)

    return swaps


def test_cases() -> None:
    print(build_heap([5, 4, 3, 2, 1]) == [(1, 4), (0, 1), (1, 3)])
    print(build_heap([1, 2, 3, 4, 5]) == [])


def main() -> None:
    n: int = int(input())
    data: List[int] = list(map(int, input().split()))
    assert len(data) == n

    swaps: List[int] = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)

    # test_cases()


if __name__ == "__main__":
    main()
