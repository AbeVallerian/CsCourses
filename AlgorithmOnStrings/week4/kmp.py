# python3
import sys


def compute_prefix_function(text):
    prefix = [0]
    border = 0

    for i in range(1, len(text)):
        while border > 0 and text[i] != text[border]:
            border = prefix[border - 1]
        if text[i] == text[border]:
            border += 1
        else:
            border = 0
        prefix.append(border)
    return prefix


def test_compute_prefix_function():
    print(compute_prefix_function("abababcaab") == [0, 0, 1, 2, 3, 4, 0, 1, 1, 2])


def find_pattern(pattern, text):
    """
    Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    result = []
    if len(pattern) > len(text):
        return result

    new_str = pattern + "$" + text
    prefix = compute_prefix_function(new_str)

    for i in range(len(pattern) + 1, len(new_str)):
        if prefix[i] == len(pattern):
            result.append(i - 2 * len(pattern))

    return result


def test_find_pattern():
    print(find_pattern("TACG", "GT") == [])
    print(find_pattern("ATA", "ATATA") == [0, 2])
    print(find_pattern("ATAT", "GATATATGCATATACTT") == [1, 3, 9])


if __name__ == "__main__":
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

    # test_compute_prefix_function()
    # test_find_pattern()
