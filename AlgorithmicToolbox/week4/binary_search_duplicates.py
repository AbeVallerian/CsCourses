from typing import List


def binary_search(
    keys: List[int], query: int, left: int = -999, right: int = -999
) -> int:
    if left == -999:
        left = 0
    if right == -999:
        right = len(keys) - 1

    while right >= left:
        mid: int = int(left + (right - left) / 2)
        if keys[mid] == query:
            rec_mid: int = binary_search(keys, query, left=left, right=mid - 1)
            if rec_mid == -1:
                rec_mid = len(keys)
            return min(mid, rec_mid)
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
    print(binary_search([2, 4, 4, 4, 7, 7, 9], 4) == 1)
    print(binary_search([2, 4, 4, 4, 7, 7, 9], 2) == 0)
    print(binary_search([2, 4, 4, 4, 7, 7, 9], 9) == 6)
    print(binary_search([2, 4, 4, 4, 7, 7, 9], 3) == -1)


if __name__ == "__main__":
    num_keys: int = int(input())
    input_keys: List[int] = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries: int = int(input())
    input_queries: List[int] = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=" ")

    # test_cases()
