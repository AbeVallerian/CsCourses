def gcd(a: int, b: int):
    a1: int = min(a, b)
    a2: int = max(a, b)
    while a2 % a1 != 1:
        if a2 % a1 == 0:
            return a1
        tmp: int = a2 % a1
        a2 = a1
        a1 = tmp
    return 1


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
