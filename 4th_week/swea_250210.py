T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    num = 1
    bottom, top = 0, N - 1
    left, right = 0, N - 1

    while num <= N * N:
        for j in range(left, right + 1):
            matrix[top][j] = num
            num += 1
        top += 1

        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1



