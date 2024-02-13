from sys import stdin
from typing import List


def min_refills(distance: int, tank: int, stops: List[int]) -> int:
    if tank >= distance:
        return 0
    if len(stops) == 0 and tank < distance:
        return -1

    max_tank: int = tank
    refuel: int = 0
    position: int = 0
    for i, _ in enumerate(stops):
        if stops[i] - position > tank:
            # cannot reach the next gas station
            return -1

        if distance - position <= tank:
            # can reach the destination
            return refuel

        if i == len(stops) - 1:
            # last stop
            if distance - stops[i] > tank:
                # cannot reach the final destination
                return -1
            elif distance - stops[i] <= tank:
                refuel += 1
                tank = max_tank
                position = stops[i]
        elif stops[i + 1] - position > tank:
            # need refuel here
            refuel += 1
            tank = max_tank
            position = stops[i]
        else:
            # no need refuel
            pass

    return refuel


def test_cases():
    print(min_refills(950, 400, [200, 375, 550, 750]) == 2)
    print(min_refills(10, 3, [1, 2, 5, 9]) == -1)
    print(min_refills(200, 250, [100, 150]) == 0)
    print(min_refills(700, 200, [100, 200, 300, 400]) == -1)


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())

    # print("d:", d)
    # print("m:", m)
    # print("stops:", stops)

    print(min_refills(d, m, stops))

    # test_cases()
