# python3
import sys


def InverseBWTNaive(bwt):
    # write your code here
    last_col = [s for s in bwt]
    sorted_last_col = list(sorted(last_col))
    final_result = sorted_last_col
    for i in range(len(bwt) - 1):
        final_result = sorted(["".join(item) for item in zip(last_col, final_result)])
    return final_result[0][1:] + "$"


def InverseBWT(bwt):
    # write your code here
    last_col = [s for s in bwt]
    sorted_last = "".join(list(sorted(last_col)))

    last_position = {
        "$": 0,
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0,
    }
    mapping = {}
    for idx, char in enumerate(sorted_last):
        mapped_idx = bwt.index(char, last_position[char])
        mapping[idx] = mapped_idx
        last_position[char] = mapped_idx + 1

    curr_idx = 0
    inverse = "$"
    for _ in range(len(bwt) - 1):
        curr_idx = mapping[curr_idx]
        inverse += sorted_last[curr_idx]

    return inverse[1:] + "$"


def test_cases():
    print(InverseBWT("AA$") == "AA$")
    print(InverseBWT("AC$A") == "ACA$")
    print(InverseBWT("AGGGAA$") == "GAGAGA$")


if __name__ == "__main__":
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))

    # test_cases()
