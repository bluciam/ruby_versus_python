def rotate_90(matrix):
    return [[ row[col] for row in matrix ] for col in range(0,len(matrix)) ]

def rotate_90_semi(matrix):
    new_mat = []
    for col in range(0,len(matrix)):
        new_mat.append( [ matrix[row][col] for row in range(0,len(matrix)) ] )
    return new_mat
    

def rotate_90_long(matrix):
    new_mat = []
    for col in range(0,len(matrix)):
        new_row = []
        for row in matrix:
            new_row.append(row[col])
        new_mat.append(new_row)
    return new_mat

def rotate_90_superlong(matrix):
    new_mat = []
    for col in range(0,len(matrix)):
        new_row = []
        for row in range(0,len(matrix)):
            new_row.append(matrix[row][col])
        new_mat.append(new_row)
    return new_mat


matrix = [
          [1,2,3,0],
          [4,5,6,0],
          [7,8,9,0],
          [0,0,0,0],
         ]

print rotate_90(matrix)
print
print rotate_90_semi(matrix)
print
print rotate_90_long(matrix)
print
print rotate_90_superlong(matrix)
