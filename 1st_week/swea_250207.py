def get_row_max(matrix):
    result = 0
    for i in range(100):
        row_sum = 0
        for j in range(100):
            row_sum += matrix[i][j]

        if row_sum > result:
            result = row_sum


    return result


def get_col_max(matrix):
    result = 0
    for i in range(100):
        col_sum = 0
        for j in range(100):
            col_sum += matrix[j][i]

        if col_sum > result:
            result = col_sum

    return result


def get_diagonal_max(matrix):
    diagonal_sum1 = 0
    diagonal_sum2 = 0
    for i in range(100):
        diagonal_sum1 += matrix[i][i]
        diagonal_sum2 += matrix[i][99 - i]

    return diagonal_sum1 if diagonal_sum1 > diagonal_sum2 else diagonal_sum2


T = 10
for t in range(1, T + 1):
    num = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    diagonal = get_diagonal_max(matrix)
    row = get_row_max(matrix)
    col = get_col_max(matrix)
    result = max(col, max(diagonal, row))

    print(f'#{t} {result}')