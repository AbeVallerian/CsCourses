from typing import List


def max_pairwise_product(numbers: List):
    numbers = sorted(numbers)
    return numbers[-1] * numbers[-2]


if __name__ == "__main__":
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))
