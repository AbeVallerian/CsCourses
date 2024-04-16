# python3
import sys


def sort_characters(text):
    distinct = {"$": 0, "A": 1, "C": 2, "G": 3, "T": 4}
    order = [0 for _ in range(len(text))]
    count = {i: 0 for i in range(len(distinct))}

    for i in range(len(text)):
        count[distinct[text[i]]] += 1
    for j in range(1, len(distinct)):
        count[j] += count[j - 1]
    for i in reversed(range(len(text))):
        c = distinct[text[i]]
        count[c] -= 1
        order[count[c]] = i

    return order


def test_sort_characters():
    print(sort_characters("CAA$") == [3, 1, 2, 0])
    print(sort_characters("GAC$") == [3, 1, 2, 0])
    print(sort_characters("ACACAA$") == [6, 0, 2, 4, 5, 1, 3])
    print(sort_characters("AACGATAGCGGTAGA$"))


def compute_char_classes(text, order):
    c_class = [0 for _ in range(len(text))]
    for i in range(1, len(text)):
        if text[order[i]] != text[order[i - 1]]:
            c_class[order[i]] = c_class[order[i - 1]] + 1
        else:
            c_class[order[i]] = c_class[order[i - 1]]

    return c_class


def test_compute_char_classes():
    print(
        compute_char_classes("ACACAA$", [6, 0, 2, 4, 5, 1, 3]) == [1, 2, 1, 2, 1, 1, 0]
    )
    text = "AACGATAGCGGTAGA$"
    print(compute_char_classes(text, sort_characters(text)))


def sort_doubled(text, l, order, c_class):
    count = [0 for _ in range(len(text))]
    new_order = [0 for _ in range(len(text))]
    for i in range(len(text)):
        count[c_class[i]] += 1
    for j in range(1, len(text)):
        count[j] += count[j - 1]
    for i in reversed(range(len(text))):
        start = ((order[i] - l + len(text) % len(text)) + len(text)) % len(text)
        cl = c_class[start]
        count[cl] -= 1
        new_order[count[cl]] = start
    return new_order


def test_sort_doubled():
    print(
        sort_doubled("ACACAA$", 1, [6, 0, 2, 4, 5, 1, 3], [1, 2, 1, 2, 1, 1, 0])
        == [6, 5, 4, 0, 2, 1, 3]
    )
    text = "AACGATAGCGGTAGA$"
    print(
        sort_doubled(
            text,
            1,
            sort_characters(text),
            compute_char_classes(text, sort_characters(text)),
        )
    )


def update_classes(new_order, c_class, l):
    n = len(new_order)
    new_class = [0 for _ in range(n)]
    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i - 1]
        mid = (cur + l + n) % n
        mid_prev = (prev + l + n) % n

        if c_class[cur] != c_class[prev] or c_class[mid] != c_class[mid_prev]:
            new_class[cur] = new_class[prev] + 1
        else:
            new_class[cur] = new_class[prev]
    return new_class


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    order = sort_characters(text)
    c_class = compute_char_classes(text, order)
    l = 1
    while l < len(text):
        order = sort_doubled(text, l, order, c_class)
        c_class = update_classes(order, c_class, l)
        l = 2 * l
    return order


def test_build_suffix_array():
    print(build_suffix_array("AAA$") == [3, 2, 1, 0])
    print(build_suffix_array("GAC$") == [3, 1, 2, 0])
    print(build_suffix_array("GAGAGAGA$") == [8, 7, 5, 3, 1, 6, 4, 2, 0])
    print(build_suffix_array("AACGATAGCGGTAGA$"))


if __name__ == "__main__":
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))

    # test_sort_characters()
    # test_compute_char_classes()
    # test_sort_doubled()
    # test_build_suffix_array()
