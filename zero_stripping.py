"""
For each zero in an mxn matrix, set its entire row and column to zero in place.
"""


def zero_strip_optimized(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    rows_to_zero = set()
    cols_to_zero = set()

    # Identify rows and columns with zeros
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)

    # Zero the identified rows and columns
    for i in range(m):
        for j in range(n):
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j] = 0


def zero_strip_optimized(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Check if first row has any zero
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first column has any zero
    for i in range(m):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row and first column as markers
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0  # Mark row
                matrix[0][j] = 0  # Mark column

    # Zero rows based on first column markers
    for i in range(1, m):
        if matrix[i][0] == 0:
            for j in range(1, n):
                matrix[i][j] = 0

    # Zero columns based on first row markers
    for j in range(1, n):
        if matrix[0][j] == 0:
            for i in range(1, m):
                matrix[i][j] = 0

    # Zero first row if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0

    # Zero first column if needed
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
