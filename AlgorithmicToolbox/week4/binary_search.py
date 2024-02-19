from typing import List


def binary_search(keys: List[int], query: int) -> int:
    left: int = 0
    right: int = len(keys) - 1
    while right >= left:
        mid: int = int(left + (right - left) / 2)
        if keys[mid] == query:
            return mid
        elif keys[mid] > query:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def test_cases() -> None:
    print(binary_search([1, 5, 8, 12, 13], 8) == 2)
    print(binary_search([1, 5, 8, 12, 13], 1) == 0)
    print(binary_search([1, 5, 8, 12, 13], 13) == 4)
    print(binary_search([1, 5, 8, 12, 13], 23) == -1)


if __name__ == "__main__":
    num_keys: int = int(input())
    input_keys: List[int] = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")

    # test_cases()
