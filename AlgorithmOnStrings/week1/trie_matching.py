# python3
import sys


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
                curr_id = tree[curr_id][char]
                try:
                    tree[curr_id]
                except:
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


def test_cases():
    print(solve("AAA", 1, ["AA"]) == [0, 1])
    print(solve("AA", 1, ["T"]) == [])
    print(solve("AATCGGGTTCAATCGGGGT", 2, ["ATCG", "GGGT"]) == [1, 4, 11, 15])


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(" ".join(map(str, ans)) + "\n")

# test_cases()
