import sys


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


def sum_per_cycle(cycle: int, m: int) -> int:
    if cycle <= 1:
        return cycle

    a0: int = 0
    a1: int = 1
    sum_last_digit: int = 1
    for _ in range(2, cycle + 1):
        tmp: int = (a0 + a1) % m
        a0 = a1
        a1 = tmp
        sum_last_digit = (sum_last_digit + a1) % m

    return sum_last_digit


def fibonacci_sum(n: int) -> int:
    if n <= 1:
        return n

    m: int = 10

    cycle: int = find_cycle(n, m)
    sum_cycle: int = sum_per_cycle(cycle, m)

    a0: int = 0
    a1: int = 1
    sum_last_digit: int = 1
    if n % cycle == 0:
        sum_last_digit = 0
    else:
        for _ in range(2, n % cycle + 1):
            tmp: int = (a0 + a1) % m
            a0 = a1
            a1 = tmp
            sum_last_digit = (sum_last_digit + a1) % m

    return (sum_last_digit + int(n / cycle) * sum_cycle) % m


def fibonacci_partial_sum(from_: int, to: int) -> int:
    if from_ == 0:
        sum_subtract: int = 0
    else:
        sum_subtract: int = fibonacci_sum(from_ - 1)
    sum_add: int = fibonacci_sum(to)

    part_sum: int = (sum_add - sum_subtract) % 10
    if part_sum < 0:
        return part_sum + 10
    return part_sum


if __name__ == "__main__":
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
