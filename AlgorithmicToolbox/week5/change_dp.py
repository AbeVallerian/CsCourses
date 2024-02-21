from typing import Dict


def change(money: int) -> int:
    change_dict: Dict = {
        0: 0,
        1: 1,
        2: 2,
        3: 1,
        4: 1,
    }

    for i in range(5, money + 1):
        change_dict[i] = min(
            change_dict[i - 1] + 1, change_dict[i - 3] + 1, change_dict[i - 4] + 1
        )

    return change_dict[money]


def test_cases() -> None:
    print(change(6) == 2)
    print(change(34) == 9)


if __name__ == "__main__":
    m: int = int(input())
    print(change(m))

    # test_cases()
