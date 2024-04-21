# Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    node_id = 1
    for pattern in patterns:
        curr_id = 0
        for char in pattern:
            try:
                curr_id = tree[curr_id][char]
            except:
                try:
                    tree[curr_id]
                    tree[curr_id][char] = node_id
                except:
                    tree[curr_id] = {char: node_id}
                finally:
                    curr_id = node_id
                    node_id += 1
    return tree


def test_cases() -> None:
    print(build_trie(["ATA"]) == {0: {"A": 1}, 1: {"T": 2}, 2: {"A": 3}})
    print(build_trie(["AT", "AG", "AC"]) == {0: {"A": 1}, 1: {"T": 2, "G": 3, "C": 4}})
    print(
        build_trie(["ATAGA", "ATC", "GAT"])
        == {
            0: {"A": 1, "G": 7},
            1: {"T": 2},
            2: {"A": 3, "C": 6},
            3: {"G": 4},
            4: {"A": 5},
            7: {"A": 8},
            8: {"T": 9},
        }
    )


if __name__ == "__main__":
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

    # test_cases()
