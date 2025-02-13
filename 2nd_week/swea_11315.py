def check(matrix):
    N = len(matrix)

    for i in range(N):
        for j in range(N - 4):
            if all(matrix[i][k] == 'o' for k in range(j, j + 5)):
                return True
            if all(matrix[k][i] == 'o' for k in range(j, j + 5)):
                return True

    for i in range(N - 4):
        for j in range(N - 4):
            if all(matrix[i + k][j + k] == 'o' for k in range(5)):
                return True
            if all(matrix[i + k][j + 4 - k] == 'o' for k in range(5)):
                return True

    return False


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(input().strip()) for _ in range(N)]
    if check(matrix):
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')
