def fibonacci_last_digit(n: int):
    if n <= 1:
        return n

    a0: int = 0
    a1: int = 1
    for _ in range(2, n + 1):
        tmp: int = (a0 + a1) % 10
        a0 = a1
        a1 = tmp

    return a1


if __name__ == "__main__":
    n: int = int(input())
    print(fibonacci_last_digit(n))
