from typing import Dict, List


def compute_operations(n: int) -> List[int]:
    compute_dict: Dict = {
        0: {"val": 0, "seq": []},
        1: {"val": 1, "seq": [1]},
        2: {"val": 2, "seq": [1, 2]},
        3: {"val": 2, "seq": [1, 3]},
    }

    for i in range(4, n + 1):
        op1: int = compute_dict[i - 1]["val"] + 1
        op2: int = 10000000 if i % 2 != 0 else compute_dict[i / 2]["val"] + 1
        op3: int = 10000000 if i % 3 != 0 else compute_dict[i / 3]["val"] + 1
        compute_dict[i] = {"val": min(op1, op2, op3)}
        if compute_dict[i]["val"] == op3:
            compute_dict[i]["seq"] = compute_dict[i / 3]["seq"] + [i]
        elif compute_dict[i]["val"] == op2:
            compute_dict[i]["seq"] = compute_dict[i / 2]["seq"] + [i]
        else:
            compute_dict[i]["seq"] = compute_dict[i - 1]["seq"] + [i]

    return compute_dict[n]["seq"]


def test_cases() -> None:
    print(compute_operations(1) == [1])
    print(compute_operations(9) == [1, 3, 9])
    print(compute_operations(10) == [1, 3, 9, 10])
    print(
        compute_operations(96234)
        == [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234]
    )


if __name__ == "__main__":
    input_n: int = int(input())
    output_sequence: List[int] = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)

    # test_cases()
