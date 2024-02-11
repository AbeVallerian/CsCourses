def change(money):
    return int(money / 10) + int((money % 10) / 5) + int(money % 5)


def test_cases():
    print(change(2) == 2)
    print(change(28) == 6)


if __name__ == "__main__":
    m = int(input())
    print(change(m))

    # test_cases()
