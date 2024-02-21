from typing import List


def edit_distance(first_string: List[int], second_string: List[int]) -> int:
    edit_distance: List[List[int]] = [
        [0 for i in range(len(second_string) + 1)] for j in range(len(first_string) + 1)
    ]

    for i in range(len(first_string) + 1):
        for j in range(len(second_string) + 1):
            if i == 0:
                edit_distance[i][j] = j
            elif j == 0:
                edit_distance[i][j] = i
            elif first_string[i - 1] == second_string[j - 1]:
                edit_distance[i][j] = edit_distance[i - 1][j - 1]
            else:
                edit_distance[i][j] = 1 + min(
                    edit_distance[i][j - 1],
                    edit_distance[i - 1][j],
                    edit_distance[i - 1][j - 1],
                )
    return edit_distance[len(first_string)][len(second_string)]


def test_cases() -> None:
    print(edit_distance("short", "ports") == 3)
    print(edit_distance("editing", "distance") == 5)
    print(edit_distance("ab", "ab") == 0)


if __name__ == "__main__":
    print(edit_distance(input(), input()))

    # test_cases()
