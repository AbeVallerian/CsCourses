# python3
import sys


def build_trie(patterns):
    tree = dict()
    # write your code here
    node_id = 1
    for pattern in patterns:
        curr_id = 0
        prev_id = 0
        for char in pattern:
            prev_id = curr_id
            try:
                curr_id, is_end = tree[curr_id][char]
            except:
                try:
                    tree[curr_id]
                    tree[curr_id][char] = (node_id, 0)
                except:
                    tree[curr_id] = {char: (node_id, 0)}
                finally:
                    curr_id = node_id
                    node_id += 1
        tree[prev_id][char] = (tree[prev_id][char][0], 1)

    return tree


def test_cases_build_trie() -> None:
    print(build_trie(["ATA"]) == {0: {"A": (1, 0)}, 1: {"T": (2, 0)}, 2: {"A": (3, 1)}})
    print(
        build_trie(["AT", "AG", "AC"])
        == {0: {"A": (1, 0)}, 1: {"T": (2, 1), "G": (3, 1), "C": (4, 1)}}
    )
    print(
        build_trie(["ATAGA", "ATC", "GAT"])
        == {
            0: {"A": (1, 0), "G": (7, 0)},
            1: {"T": (2, 0)},
            2: {"A": (3, 0), "C": (6, 1)},
            3: {"G": (4, 0)},
            4: {"A": (5, 1)},
            7: {"A": (8, 0)},
            8: {"T": (9, 1)},
        }
    )
    print(
        build_trie(["AT", "A", "AG"])
        == {0: {"A": (1, 1)}, 1: {"T": (2, 1), "G": (3, 1)}}
    )


def solve(text, n, patterns):
    tree = build_trie(patterns)

    result = []
    if len(tree) == 0:
        return result

    # write your code here
    for i in range(len(text)):
        curr_id = 0
        for j, char in enumerate(text[i:]):
            try:
                curr_id, is_end = tree[curr_id][char]
                if is_end == 1:
                    result.append(i)
                    break
            except:
                try:
                    tree[curr_id]
                    break
                except:
                    if curr_id == 0:
                        break
                    else:
                        result.append(i)
                        break
    return result


def test_cases_solve():
    print(solve("AAA", 1, ["AA"]) == [0, 1])
    print(solve("AA", 1, ["T"]) == [])
    print(solve("AATCGGGTTCAATCGGGGT", 2, ["ATCG", "GGGT"]) == [1, 4, 11, 15])
    print(solve("ACATA", 3, ["AT", "A", "AG"]) == [0, 2, 4])


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(" ".join(map(str, ans)) + "\n")

# test_cases_build_trie()
# test_cases_solve()
