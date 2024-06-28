# python3


def read_data(numreads):
    reads = set()
    for _ in range(numreads):
        reads.add(input().strip())
    return sorted(reads)


def compare_two_strings(s1, s2, start=1):
    overlap = 0
    for i in range(start, len(s2)):
        if s2[:i] == s1[-i:]:
            overlap = i
    return overlap


def find_max_overlap(data, best_match):
    first = data.pop(0)
    result = first
    last_match = first

    while len(data) > 0:
        max_overlap = 0
        max_r = ""
        max_i = -1
        flag_break = False
        for i, r in enumerate(data):
            overlap = compare_two_strings(last_match, r, start=max_overlap + 1)
            if max_overlap < overlap:
                max_overlap = overlap
                max_r = r
                max_i = i
            if max_overlap == best_match:
                result += max_r[max_overlap:]
                last_match = max_r
                max_overlap = 0
                max_r = ""
                data.pop(max_i)
                flag_break = True
                break

        if max_overlap > 0:
            result += max_r[max_overlap:]
            last_match = max_r
            max_overlap = 0
            max_r = ""
            data.pop(max_i)
        elif flag_break:
            continue
        else:
            break

    overlap = compare_two_strings(last_match, first)
    return result[:-overlap]


def test_compare_two_strings():
    assert compare_two_strings("AAC", "ACG") == 2
    assert compare_two_strings("ACG", "GTT") == 1
    assert compare_two_strings("AAC", "GAA") == 0


def test_find_max_overlap():
    data = ["AAC", "ACG", "GTT", "GAA", "TCG"]
    assert find_max_overlap(data, 2) == "AACGTTCG"

    data = ["ACGTT", "CGTTC", "GTTCG", "TTCGA"]
    assert find_max_overlap(data, 4) == "ACGTTCG"


# test_compare_two_strings()
# test_find_max_overlap()

if __name__ == "__main__":
    data = read_data(numreads=1608)
    print(find_max_overlap(data, 99))
