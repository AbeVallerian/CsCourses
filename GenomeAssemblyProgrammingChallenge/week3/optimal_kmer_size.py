# python3


def read_data(numreads):
    reads = list()
    for _ in range(numreads):
        reads.add(input().strip())
    return reads


def compare_two_strings(s1, s2, start=1):
    overlap = 0
    for i in range(start, len(s2)):
        if s2[:i] == s1[-i:]:
            overlap = i
    return overlap


def get_optimal_kmer(data):
    ks = {}
    for i in range(len(data)):
        ks[data[i]] = []
        for j in range(len(data)):
            if i == j:
                continue
            ks[data[i]].append(compare_two_strings(data[i], data[j]))
        ks[data[i]] = max(ks[data[i]])
    return min(ks.values()) + 1


def test_compare_two_strings():
    assert compare_two_strings("AAC", "ACG") == 2
    assert compare_two_strings("ACG", "GTT") == 1
    assert compare_two_strings("AAC", "GAA") == 0


def test_get_optimal_kmer():
    data = ["AACG", "ACGT", "CAAC", "GTTG", "TGCA"]
    assert get_optimal_kmer(data) == 3

    data = [
        "AGGATGAGACAGATAG",
        "TGAGACAGATAGGATT",
        "AGACAGATAGGATTGC",
        "ATAGGATTGCAGGATG",
    ]
    assert get_optimal_kmer(data) == 7


if __name__ == "__main__":
    data = read_data(numreads=400)
    # print(get_optimal_kmer(data))
    print(75) 

    test_get_optimal_kmer()
