from typing import List


def largest_number(numbers: List[int]) -> int:
    numbers: List[str] = list(map(str, numbers))

    d1_numbers: List[str] = []
    d2_numbers: List[str] = []
    d3_numbers: List[str] = []
    for num in numbers:
        d1: int = int(num[0])
        d1_numbers.append(d1)

        if len(num) == 1:
            d2_numbers.append(d1)
        else:
            d2_numbers.append(int(num[1]))
        d2: int = d2_numbers[-1]

        if len(num) <= 2:
            if d2 > d1:
                d3_numbers.append(int(d1) + 0.5)
            else:
                d3_numbers.append(int(d1) - 0.5)
        else:
            d3_numbers.append(int(num[2]))

    z_numbers: List = sorted(
        zip(numbers, d1_numbers, d2_numbers, d3_numbers),
        key=lambda x: (x[1], x[2], x[3]),
        reverse=True,
    )
    # print(z_numbers)

    largest: List[str] = []
    for item in z_numbers:
        largest.append(item[0])

    return int("".join(largest))


def test_cases() -> None:
    print(largest_number([21, 2]) == 221)
    print(largest_number([9, 4, 6, 1, 9]) == 99641)
    print(largest_number([23, 39, 92]) == 923923)
    print(largest_number([23]) == 23)
    print(largest_number([23, 239]) == 23923)
    print(largest_number([2, 23, 21, 235, 231]) == 23523231221)
    print(largest_number([232, 23]) == 23232)
    print(largest_number([919, 91]) == 91991)
    print(largest_number([818, 81]) == 81881)


if __name__ == "__main__":
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))

    # test_cases()
