# 20-01-16
# EX 23.7

row, col = map(int, input().split())
matrix = []
for i in range(row):
    while True:
        col_one = list(input())
        if len(col_one) == col and col_one.count('*') + col_one.count('.') == col:
            matrix.append(col_one)
            break
print()

matrix_answer = matrix.copy()

for i in range(row):
    matrix_answer[i].insert(col, '.')
    matrix_answer[i].insert(0, '.')

matrix_answer.insert(row, list('.' * (col + 2)))
matrix_answer.insert(0, list('.' * (col + 2)))

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if matrix_answer[i][j] == '.':
            eight_way = [ matrix_answer[i-1][j-1],
                          matrix_answer[i-1][j+0],
                          matrix_answer[i-1][j+1],
                          matrix_answer[i+0][j-1],
                          matrix_answer[i+0][j+1],
                          matrix_answer[i+1][j-1],
                          matrix_answer[i+1][j+0],
                          matrix_answer[i+1][j+1] ]
            matrix_answer[i][j] = str(eight_way.count('*'))

for i in range(1, len(matrix) + 1):
    print(''.join(matrix_answer[i])[1:-1])


