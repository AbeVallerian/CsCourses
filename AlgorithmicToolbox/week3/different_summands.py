from typing import List


def optimal_summands(n: int) -> List[int]:
    summands: List[int] = []
    num: int = 0
    sum: int = 0
    while sum < n:
        num += 1
        summands.append(num)
        sum += num

    if sum > n:
        summands.pop()
        sum -= num
        if len(summands) > 0:
            summands[-1] += n - sum
        else:
            summands.append(n - sum)
    return summands


# def test_cases() -> None:
#     print(optimal_summands(6) == [1, 2, 3])
#     print(optimal_summands(8) == [1, 2, 5])
#     print(optimal_summands(2) == [2])


if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)

    # test_cases()
