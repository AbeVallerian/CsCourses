def find_cycle(n: int, m: int) -> int:
    a0: int = 0
    a1: int = 1
    a0_init: int = a0
    a1_init: int = a1
    cycle: int = 0
    for i in range(2, n + 1):
        tmp: int = (a0 + a1) % m
        a0 = a1
        a1 = tmp
        if a0 == a0_init and a1 == a1_init:
            cycle = i - 1
            break
    if cycle == 0:
        return n + 1
    return cycle


def fibonacci_huge_naive(n: int, m: int) -> int:
    if n <= 1:
        return n % m

    a0 = 0
    a1 = 1
    for _ in range(2, n + 1):
        tmp = (a0 + a1) % m
        a0 = a1
        a1 = tmp

    return a1


if __name__ == "__main__":
    n, m = map(int, input().split())
    cycle: int = find_cycle(n, m)
    print(fibonacci_huge_naive(n % cycle, m))
