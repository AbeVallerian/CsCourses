from collections import deque
from typing import Deque, List, Tuple


def hash_func(s: str, multiplier: int, prime: int) -> int:
    ans: int = 0
    for c in reversed(s):
        ans = (ans * multiplier + ord(c)) % prime
    return ans


def read_input() -> Tuple[str, str]:
    return (input().rstrip(), input().rstrip())


def print_occurrences(output: List[int]) -> None:
    print(" ".join(map(str, output)))


def get_occurrences(
    pattern: str,
    text: str,
    bucket_count: int = 800,
    multiplier: int = 263,
    prime: int = 1000000007,
) -> List[int]:
    h_pattern: int = hash_func(pattern, multiplier, prime) % bucket_count
    occur: Deque[int] = deque()

    y: int = 1
    for _ in range(len(pattern)):
        y = (y * multiplier) % prime

    hashed: int = -1
    for i in reversed(range(len(text) - len(pattern) + 1)):
        if hashed == -1:
            hashed = hash_func(text[i : i + len(pattern)], multiplier, prime)
        else:
            hashed = (
                hashed * multiplier + (ord(text[i]) - ord(text[i + len(pattern)]) * y)
            ) % prime

        if hashed % bucket_count == h_pattern:
            if text[i : i + len(pattern)] == pattern:
                occur.appendleft(i)
    return list(occur)


def test_cases() -> None:
    print(get_occurrences("aba", "abacaba") == [0, 4])
    print(get_occurrences("Test", "testTesttesT") == [4])
    print(get_occurrences("aaaaa", "baaaaaaa") == [1, 2, 3])


if __name__ == "__main__":
    print_occurrences(get_occurrences(*read_input()))

    # test_cases()
