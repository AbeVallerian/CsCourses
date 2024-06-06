# python3
from sys import stdin


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def SelectPivotElement(a, b, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)

    min_val = None
    min_idx = None
    for i, s in enumerate(a[-1]):
        if s < 0 and not used_columns[i]:
            if min_idx is None or s < min_val:
                min_idx = i
                min_val = s
    pivot_element.column = min_idx
    if min_idx is None:
        return Position(-1, -1)

    min_val = None
    min_idx = None
    for i in range(len(a) - 1):
        if not used_rows[i]:
            if a[i][pivot_element.column] == 0:
                pass
            elif b[i] / a[i][pivot_element.column] < 0:
                pass
            elif min_idx is None or b[i] / a[i][pivot_element.column] < min_val:
                min_idx = i
                min_val = b[i] / a[i][pivot_element.column]
    pivot_element.row = min_idx
    if min_idx is None:
        return Position(-1, -1)

    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = (
        a[pivot_element.row],
        a[pivot_element.column],
    )
    b[pivot_element.column], b[pivot_element.row] = (
        b[pivot_element.row],
        b[pivot_element.column],
    )
    used_rows[pivot_element.column], used_rows[pivot_element.row] = (
        used_rows[pivot_element.row],
        used_rows[pivot_element.column],
    )
    pivot_element.row = pivot_element.column
    return a, b, used_rows, pivot_element


def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
    coef = a[pivot_element.row][pivot_element.column]
    for i in range(len(a[pivot_element.row])):
        a[pivot_element.row][i] /= coef
    b[pivot_element.row] /= coef

    for i in range(len(b)):
        if i != pivot_element.row:
            mult = a[i][pivot_element.column]
            for j in range(len(a[0])):
                a[i][j] -= mult * a[pivot_element.row][j]
            b[i] -= mult * b[pivot_element.row]
    return a, b


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True
    return used_rows, used_columns


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * len(equation.a[0])
    used_rows = [False] * size
    for step in range(size):
        print("step", step)
        pivot_element = SelectPivotElement(a, b, used_rows, used_columns)
        print(pivot_element.row, pivot_element.column)
        if pivot_element.row < 0:
            break
        a, b, used_rows, pivot_element = SwapLines(a, b, used_rows, pivot_element)
        a, b = ProcessPivotElement(a, b, pivot_element)
        used_rows, used_columns = MarkPivotElementUsed(
            pivot_element, used_rows, used_columns
        )
        print(a)
        print(b)

    return b


def solve_diet_problem(n, m, A, b, c):
    # Write your code here
    for i in range(n):
        for j in range(len(A)):
            if i == j:
                A[j] += [1]
            else:
                A[j] += [0]

    for j in range(len(A)):
        A[j] += [0]
    tmp = [-t for t in c]
    for i in range(n):
        tmp += [0]
    tmp += [1]
    A += [tmp]

    b += [0]

    eq = Equation(A, b)

    sol = SolveEquation(eq)

    return [0, sol]


def test_cases():
    # n = 2
    # m = 2
    # A = [
    #     [1, 1],
    #     [2, 1],
    # ]
    # b = [12, 16]
    # c = [40, 30]
    # _, sol = solve_diet_problem(n, m, A, b, c)
    # assert sol == [4, 8, 400]

    # n = 2
    # m = 2
    # A = [
    #     [2, 1],
    #     [2, 3],
    # ]
    # b = [8, 12]
    # c = [3, 1]
    # _, sol = solve_diet_problem(n, m, A, b, c)
    # assert sol == [4, 4, 12]

    n = 3
    m = 2
    A = [
        [2, 1],
        [3, 4],
        [4, 7],
    ]
    b = [300, 509, 812]
    c = [50, 60]
    _, sol = solve_diet_problem(n, m, A, b, c)
    assert sol == [691 / 5, 118 / 5, 8326]

    n = 3
    m = 2
    A = [
        [-1, -1],
        [1, 0],
        [0, 1],
    ]
    b = [-1, 2, 2]
    c = [-1, 2]
    _, sol = solve_diet_problem(n, m, A, b, c)


# n, m = list(map(int, stdin.readline().split()))
# A = []
# for i in range(n):
#     A += [list(map(int, stdin.readline().split()))]
# b = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))

# anst, ansx = solve_diet_problem(n, m, A, b, c)

# if anst == -1:
#     print("No solution")
# if anst == 0:
#     print("Bounded solution")
#     print(" ".join(list(map(lambda x: "%.18f" % x, ansx))))
# if anst == 1:
#     print("Infinity")

test_cases()
