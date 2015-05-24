def zeroing(matrix):
    print "Before..."
    print_mat(matrix)
    list_col = []
    list_row = []
    for row_i, row in enumerate(matrix):
        for col_i, val in enumerate(row):
            if val == 0:
                list_col.append(col_i)
                list_row.append(row_i)

    set_col = set(list_col)
    set_row = set(list_row)

    cols = len(matrix[0])
    rows = len(matrix)

    for row_i in set_row:
        for i in range(cols):
            matrix[row_i][i] = 0

    for col_i in set_col:
        for i in range(rows):
            matrix[i][col_i] = 0

    print "After..."
    print_mat(matrix)
    return matrix

def print_mat(matrix):
    print
    for row in matrix:
        print row
    print

matrix = [
          [1,2,3,3],
          [4,5,6,8],
          [7,0,9,1],
          [6,5,9,1],
         ]

zeroing(matrix)
