"""
Write an algorithm such that if an element in an M x N matrix is 0, it's entire row and column are set to 0
"""


def set_row_col_zero(matrix):
    rows_lst = []
    cols_lst = []
    rows = len(matrix)  # 3 rows in your example
    cols = len(matrix[0])  # 2 columns in your example
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                rows_lst.append(i)
                cols_lst.append(j)

    for i in range(rows):
        for j in range(cols):
            if i in rows_lst or j in cols_lst:
                matrix[i][j] = 0

    print(matrix)
    return matrix


set_row_col_zero([[0, 1, 2], [1, 2, 3], [4, 5, 6]])
set_row_col_zero([[1, 2, 0], [1, 2, 3], [4, 5, 6]])
set_row_col_zero([[1, 2, 3], [1, 0, 3], [4, 5, 6]])
set_row_col_zero([[1, 2], [0, 3], [5, 6]])
