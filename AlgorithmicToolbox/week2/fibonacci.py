def fibonacci_number(n: int):
    if n <= 1:
        return n

    a0: int = 0
    a1: int = 1
    for _ in range(2, n + 1):
        tmp: int = a0 + a1
        a0 = a1
        a1 = tmp
    return a1


if __name__ == "__main__":
    input_n: int = int(input())
    print(fibonacci_number(input_n))
