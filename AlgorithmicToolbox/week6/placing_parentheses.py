import re
from typing import List


def evaluate(a: int, b: int, op: str) -> int:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        assert False


def get_min_value(
    first_idx: List[int],
    second_idx: List[int],
    op: str,
    max_list: List[List[int]],
    min_list: List[List[int]],
) -> int:
    return min(
        evaluate(
            max_list[first_idx[0]][first_idx[1]],
            max_list[second_idx[0]][second_idx[1]],
            op,
        ),
        evaluate(
            max_list[first_idx[0]][first_idx[1]],
            min_list[second_idx[0]][second_idx[1]],
            op,
        ),
        evaluate(
            min_list[first_idx[0]][first_idx[1]],
            max_list[second_idx[0]][second_idx[1]],
            op,
        ),
        evaluate(
            min_list[first_idx[0]][first_idx[1]],
            min_list[second_idx[0]][second_idx[1]],
            op,
        ),
    )


def get_max_value(
    first_idx: List[int],
    second_idx: List[int],
    op: str,
    max_list: List[List[int]],
    min_list: List[List[int]],
) -> int:
    return max(
        evaluate(
            max_list[first_idx[0]][first_idx[1]],
            max_list[second_idx[0]][second_idx[1]],
            op,
        ),
        evaluate(
            max_list[first_idx[0]][first_idx[1]],
            min_list[second_idx[0]][second_idx[1]],
            op,
        ),
        evaluate(
            min_list[first_idx[0]][first_idx[1]],
            max_list[second_idx[0]][second_idx[1]],
            op,
        ),
        evaluate(
            min_list[first_idx[0]][first_idx[1]],
            min_list[second_idx[0]][second_idx[1]],
            op,
        ),
    )


def maximum_value(dataset: str) -> int:
    inputs: List[int] = list(map(int, re.split(r"\+|-|\*", dataset)))
    ops: List[str] = re.findall(r"\+|-|\*", dataset)

    max_val: List[List[int]] = [
        [0 for j, _ in enumerate(inputs)] for i, _ in enumerate(inputs)
    ]
    min_val: List[List[int]] = [
        [0 for j, _ in enumerate(inputs)] for i, _ in enumerate(inputs)
    ]
    for step, _ in enumerate(inputs):
        for i in range(len(inputs) - step):
            j = i + step
            if i == j:
                max_val[i][j] = inputs[i]
                min_val[i][j] = inputs[i]
            elif step == 1:
                max_val[i][j] = evaluate(inputs[i], inputs[j], ops[i])
                min_val[i][j] = evaluate(inputs[i], inputs[j], ops[i])
            else:
                min_tmp: List[int] = []
                max_tmp: List[int] = []
                for sub in range(i, j):
                    min_tmp.append(
                        get_min_value(
                            [i, sub],
                            [sub + 1, j],
                            ops[sub],
                            max_list=max_val,
                            min_list=min_val,
                        )
                    )
                    max_tmp.append(
                        get_max_value(
                            [i, sub],
                            [sub + 1, j],
                            ops[sub],
                            max_list=max_val,
                            min_list=min_val,
                        )
                    )
                max_val[i][j] = max(max_tmp)
                min_val[i][j] = min(min_tmp)

    return max_val[0][-1]


def test_cases() -> None:
    print(maximum_value("1") == 1)
    print(maximum_value("3+5") == 8)
    print(maximum_value("8-5*3") == 9)
    print(maximum_value("3+2*4") == 20)
    print(maximum_value("5-8+7*4-8+9") == 200)


if __name__ == "__main__":
    print(maximum_value(input()))

    # test_cases()
