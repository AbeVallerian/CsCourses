import sys
from collections import namedtuple

Answer = namedtuple("answer_type", "i j len")


class Hash:

    def __init__(self, s, p, mod):
        self.n = len(s)
        self.hash = [0] * self.n
        self.inv_mod = [0] * self.n
        self.mod = mod
        self.p = p

        p_pow = 1
        hash_value = 0

        for i in range(self.n):
            c = ord(s[i]) - 65 + 1
            hash_value = (hash_value + c * p_pow) % self.mod
            self.hash[i] = hash_value
            self.inv_mod[i] = pow(p_pow, self.mod - 2, self.mod)
            p_pow = (p_pow * self.p) % self.mod

    def get_hash(self, l, r):
        if l == 0:
            return self.hash[r]
        window = (self.hash[r] - self.hash[l - 1]) % self.mod
        return (window * self.inv_mod[l]) % self.mod


def solve(s, t):
    def _match(k):
        if k == 0:
            return [0, 0], True

        hash_map = dict()
        for i in range(len(s) - k + 1):
            h1 = hash_s1.get_hash(i, i + k - 1)
            h2 = hash_s2.get_hash(i, i + k - 1)
            hash_map[(h1, h2)] = i

        for i in range(len(t) - k + 1):
            h1 = hash_t1.get_hash(i, i + k - 1)
            h2 = hash_t2.get_hash(i, i + k - 1)
            try:
                return [hash_map[(h1, h2)], i], True
            except:
                pass
        return [0, 0], False

    p1, p2 = 41, 43
    m1, m2 = pow(10, 9) + 9, pow(10, 9) + 7

    hash_s1 = Hash(s, p1, m1)
    hash_s2 = Hash(s, p2, m2)

    hash_t1 = Hash(t, p1, m1)
    hash_t2 = Hash(t, p2, m2)

    low, high = 0, min(len(s), len(t))

    result = [0, 0]
    length = 0
    while low <= high:
        mid = (low + high) // 2
        tmp, matched = _match(mid)
        if matched:
            result = tmp
            length = mid

            low = mid + 1
        else:
            high = mid - 1

    if length == 0:
        return Answer(0, 0, 0)
    else:
        return Answer(result[0], result[1], length)


def test_cases():
    assert solve("cool", "toolbox") == Answer(1, 1, 3)
    assert solve("aaa", "bb") == Answer(0, 0, 0)
    assert solve("aabaa", "babbaab") == Answer(0, 4, 3) or solve(
        "aabaa", "babbaab"
    ) == Answer(2, 3, 3)
    assert solve(
        "voteforthegreatalbaniaforyou", "choosethegreatalbanianfuture"
    ) == Answer(7, 6, 15)
    assert solve("aabaabbbabbaaaaba", "aabaababaaababababab") == Answer(0, 0, 6)


for line in sys.stdin.readlines():
    s, t = line.split()
    ans = solve(s, t)
    print(ans.i, ans.j, ans.len)

# test_cases()
