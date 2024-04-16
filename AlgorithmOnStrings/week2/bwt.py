# python3
import sys


def BWT(text):
    matrix = [text[i:] + text[:i] for i in range(len(text))]
    matrix.sort()
    return "".join([item[-1] for item in matrix])


def test_cases():
    print(BWT("AA$") == "AA$")
    print(BWT("ACACACAC$") == "CCCC$AAAA")
    print(BWT("AGACATA$") == "ATG$CAAA")


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(BWT(text))

    # test_cases()
