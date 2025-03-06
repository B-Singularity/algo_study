def solve(row, n, cols, diag1, diag2):
    if row == n:
        return 1

    count = 0
    for col in range(n):
        if cols[col] or diag1[(row - col)] or diag2[(row + col)]:
            continue

        cols[col] = True
        diag1[row - col] = True
        diag2[row + col] = True

        count += solve(row + 1, n, cols, diag1, diag2)

        cols[col] = False
        diag1[row - col] = False
        diag2[row + col] = False

    return count



N = int(input())
cols = [False] * N
diag1 = [False] * (2 * N - 1)
diag2 = [False] * (2 * N - 1)
count = solve(0, N, cols, diag1, diag2)
print(count)

