from typing import Dict, List


def majority_element_naive(elements: List[int]) -> int:
    majority: float = len(elements) / 2
    counter: Dict = {}
    for e in elements:
        counter[e] = counter.get(e, 0) + 1
        if counter[e] > majority:
            return 1

    return 0


def test_cases() -> None:
    print(majority_element_naive([2, 3, 9, 2, 2]) == 1)
    print(majority_element_naive([1, 2, 3, 1]) == 0)


if __name__ == "__main__":
    input_n: int = int(input())
    input_elements: List[int] = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))

    # test_cases()
