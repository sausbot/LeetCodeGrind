"""
Design an algorithm to determine if someone has won a game of tic-tac-toe
"""


def tic_tac_toe(grid: list):
    # The game is won when there are three matching elements in a row, column, or along a diagonal
    # There are 3 rows, 3 colums, and two diagonals to check

    # [[(0,0), (0,1), (0,2)],
    # [(1,0), (1,1), (1,2)],
    # [(2,0), (2,1), (2,2)]]

    x_wins = is_win(grid, "x")
    o_wins = is_win(grid, "o")

    if not x_wins and not o_wins:
        print("TIE")
    elif x_wins:
        print("X WIN")
    elif o_wins:
        print("O WINS")


def is_win(grid: list, element: str):
    # Check rows
    for i in range(3):
        if grid[i][0] == element and grid[i][1] == element and grid[i][2] == element:
            return True
    # Check cols
    for i in range(3):
        if grid[0][i] == element and grid[1][i] == element and grid[2][i] == element:
            return True
    # Check diagonals
    if (grid[0][0] == element and grid[1][1] == element and grid[2][2] == element) or (
        grid[0][2] == element and grid[1][1] == element and grid[2][0] == element
    ):
        return True

    return False


tic_tac_toe(
    [
        ["x", "x", "x"],
        ["o", "o", "x"],
        [
            "x",
            "o",
            "o",
        ],
    ]
)

tic_tac_toe(
    [
        ["x", "o", "x"],
        ["o", "o", "x"],
        [
            "x",
            "o",
            "o",
        ],
    ]
)

tic_tac_toe(
    [
        ["x", "o", "x"],
        ["o", "x", "x"],
        [
            "x",
            "o",
            "x",
        ],
    ]
)

tic_tac_toe(
    [
        ["x", "x", "o"],
        ["o", "o", "x"],
        [
            "x",
            "o",
            "x",
        ],
    ]
)
