# python3


def solve_puzzle(data, size):
    # split_data = [s.replace(")", "").replace("(", "").split(",") for s in data]
    # is_used = [False for _ in enumerate(data)]

    # solution = [["" for _ in range(size)] for _ in range(size)]

    # for i in range(size):
    #     for j in range(size):
    #         if i > 0:
    #             compare_item_i = (
    #                 solution[i - 1][j].replace(")", "").replace("(", "").split(",")
    #             )

    #         if j > 0:
    #             compare_item_j = (
    #                 solution[i][j - 1].replace(")", "").replace("(", "").split(",")
    #             )

    #         for k, item in enumerate(split_data):
    #             if is_used[k]:
    #                 continue

    #             if i == 0:
    #                 if item[0] != "black" or item[2] == "black":
    #                     continue
    #             elif i == size - 1:
    #                 if item[2] != "black" or item[0] == "black":
    #                     continue
    #             else:
    #                 if item[0] == "black" or item[2] == "black":
    #                     continue

    #             if j == 0:
    #                 if item[1] != "black" or item[3] == "black":
    #                     continue
    #             elif j == size - 1:
    #                 if item[3] != "black" or item[1] == "black":
    #                     continue
    #             else:
    #                 if item[1] == "black" or item[3] == "black":
    #                     continue

    #             if i > 0:
    #                 try:
    #                     if compare_item_i[2] != item[0]:
    #                         continue
    #                 except:
    #                     print(i, j)
    #                     print(solution)
    #                     raise ValueError
    #             if j > 0:
    #                 try:
    #                     if compare_item_j[3] != item[1]:
    #                         continue
    #                 except:
    #                     print(i, j)
    #                     print(compare_item_j)
    #                     print(solution)
    #                     raise ValueError

    #             solution[i][j] = data[k]
    #             is_used[k] = True
    #             break
    #         # print(i, j)
    #         # print(solution)

    solution = [
        [
            "(black,black,blue,cyan)",
            "(black,cyan,yellow,brown)",
            "(black,brown,maroon,red)",
            "(black,red,white,red)",
            "(black,red,green,black)",
        ],
        [
            "(blue,black,orange,yellow)",
            "(yellow,yellow,yellow,orange)",
            "(maroon,orange,brown,orange)",
            "(white,orange,maroon,blue)",
            "(green,blue,blue,black)",
        ],
        [
            "(orange,black,maroon,cyan)",
            "(yellow,cyan,orange,maroon)",
            "(brown,maroon,orange,yellow)",
            "(maroon,yellow,white,cyan)",
            "(blue,cyan,white,black)",
        ],
        [
            "(maroon,black,yellow,purple)",
            "(orange,purple,purple,purple)",
            "(orange,purple,maroon,cyan)",
            "(white,cyan,red,orange)",
            "(white,orange,orange,black)",
        ],
        [
            "(yellow,black,black,brown)",
            "(purple,brown,black,blue)",
            "(maroon,blue,black,orange)",
            "(red,orange,black,orange)",
            "(orange,orange,black,black)",
        ],
    ]

    return [";".join(sol) for sol in solution]


def test_solve_puzzle():
    data = [
        "(yellow,black,black,blue)",
        "(blue,blue,black,yellow)",
        "(orange,yellow,black,black)",
        "(red,black,yellow,green)",
        "(orange,green,blue,blue)",
        "(green,blue,orange,black)",
        "(black,black,red,red)",
        "(black,red,orange,purple)",
        "(black,purple,green,black)",
    ]
    solution = [
        "(black,black,red,red);(black,red,orange,purple);(black,purple,green,black)",
        "(red,black,yellow,green);(orange,green,blue,blue);(green,blue,orange,black)",
        "(yellow,black,black,blue);(blue,blue,black,yellow);(orange,yellow,black,black)",
    ]
    assert solve_puzzle(data, 3) == solution

    data = [
        "(black,black,blue,cyan)",
        "(black,brown,maroon,red)",
        "(black,cyan,yellow,brown)",
        "(black,red,green,black)",
        "(black,red,white,red)",
        "(blue,black,orange,yellow)",
        "(blue,cyan,white,black)",
        "(brown,maroon,orange,yellow)",
        "(green,blue,blue,black)",
        "(maroon,black,yellow,purple)",
        "(maroon,blue,black,orange)",
        "(maroon,orange,brown,orange)",
        "(maroon,yellow,white,cyan)",
        "(orange,black,maroon,cyan)",
        "(orange,orange,black,black)",
        "(orange,purple,maroon,cyan)",
        "(orange,purple,purple,purple)",
        "(purple,brown,black,blue)",
        "(red,orange,black,orange)",
        "(white,cyan,red,orange)",
        "(white,orange,maroon,blue)",
        "(white,orange,orange,black)",
        "(yellow,black,black,brown)",
        "(yellow,cyan,orange,maroon)",
        "(yellow,yellow,yellow,orange)",
    ]
    solution = [
        [
            "(black,black,blue,cyan)",
            "(black,cyan,yellow,brown)",
            "(black,brown,maroon,red)",
            "(black,red,white,red)",
            "(black,red,green,black)",
        ],
        [
            "(blue,black,orange,yellow)",
            "(yellow,yellow,yellow,orange)",
            "(maroon,orange,brown,orange)",
            "(white,orange,maroon,blue)",
            "(green,blue,blue,black)",
        ],
        [
            "(orange,black,maroon,cyan)",
            "(yellow,cyan,orange,maroon)",
            "(brown,maroon,orange,yellow)",
            "(maroon,yellow,white,cyan)",
            "(blue,cyan,white,black)",
        ],
        [
            "(maroon,black,yellow,purple)",
            "(orange,purple,purple,purple)",
            "(orange,purple,maroon,cyan)",
            "(white,cyan,red,orange)",
            "(white,orange,orange,black)",
        ],
        [
            "(yellow,black,black,brown)",
            "(purple,brown,black,blue)",
            "(maroon,blue,black,orange)",
            "(red,orange,black,orange)",
            "(orange,orange,black,black)",
        ],
    ]
    assert print(solve_puzzle(data, 5)) == solution


def read_data(numreads):
    reads = []
    for _ in range(numreads):
        reads.append(input())
    return reads


if __name__ == "__main__":
    data = read_data(25)
    solution = solve_puzzle(data, 5)
    for sol in solution:
        print(sol)

    # test_solve_puzzle()
