from sys import stdin
from typing import List


def optimal_value(capacity: int, weights: List[float], values: List[float]):
    value: float = 0.0

    values_per_weight: List[float] = []
    for i in range(len(weights)):
        values_per_weight.append(values[i] / weights[i])

    zip_list: List = sorted(list(zip(values_per_weight, weights, values)), reverse=True)

    idx: int = 0
    while capacity > 0 and idx < len(values):
        if zip_list[idx][1] >= capacity:
            value += capacity * zip_list[idx][2] / zip_list[idx][1]
            capacity = 0
        else:
            value += zip_list[idx][2]
            capacity -= zip_list[idx][1]
        idx += 1

    return value


def test_cases() -> None:
    print(optimal_value(10, [30], [500]) == 500 / 3)
    print(optimal_value(50, [20, 50, 30], [60, 100, 120]) == 180)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))

    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]

    # print("n:", n)
    # print("capacity:", capacity)
    # print("values:", values)
    # print("weights:", weights)

    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

    # test_cases()
