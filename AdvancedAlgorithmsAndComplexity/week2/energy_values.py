# python3

EPS = 1e-6
PRECISION = 20


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


def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_columns[pivot_element.column]:
        pivot_element.column += 1
    while (
        used_rows[pivot_element.row] or a[pivot_element.row][pivot_element.column] == 0
    ):
        pivot_element.row += 1

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

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        a, b, used_rows, pivot_element = SwapLines(a, b, used_rows, pivot_element)
        a, b = ProcessPivotElement(a, b, pivot_element)
        used_rows, used_columns = MarkPivotElementUsed(
            pivot_element, used_rows, used_columns
        )

    return b


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


def test_cases():
    a = [
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1],
    ]
    b = [1, 5, 4, 3]
    eq = Equation(a, b)
    sol = SolveEquation(eq)
    sol = [round(s, 6) for s in sol]
    assert sol == [1, 5, 4, 3]

    a = [
        [1, 0, 0, 0],
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
    ]
    b = [1, 4, 5, 3]
    eq = Equation(a, b)
    sol = SolveEquation(eq)
    sol = [round(s, 6) for s in sol]
    assert sol == [1, 5, 4, 3]

    a = [
        [1, 1],
        [2, 3],
    ]
    b = [3, 7]
    eq = Equation(a, b)
    sol = SolveEquation(eq)
    sol = [round(s, 6) for s in sol]
    assert sol == [2, 1]

    a = [
        [5, -5],
        [-1, -2],
    ]
    b = [-1, -1]
    eq = Equation(a, b)
    sol = SolveEquation(eq)
    sol = [round(s, 6) for s in sol]
    assert sol == [0.2, 0.4]


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)

    # test_cases()
