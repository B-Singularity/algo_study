def check(arr, y_start, y_end, x_start, x_end):
    first = arr[y_start][x_start]
    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            if arr[i][j] != first:
                return False
    return True

def recur(arr, y_start, y_end, x_start, x_end):
    if y_start == y_end:
        if arr[y_start][x_start] == '0':
            return '0'
        else:
            return '1'
    mid_x = x_start + (x_end - x_start) // 2
    mid_y = y_start + (y_end - y_start) // 2
    if check(arr, y_start, y_end, x_start, x_end):
        if arr[y_start][x_start] == '0':
            return '0'
        else:
            return '1'
    else:
        return '(' + recur(arr, y_start, mid_y, x_start, mid_x) + recur(arr, y_start, mid_y, mid_x, x_end) + recur(arr, mid_y, y_end, x_start, mid_x) + recur(arr, mid_y, y_end, mid_x, x_end) + ')'




N = int(input())
matrix = list(input() for _ in range(N))
result = recur(matrix, 0, N, 0, N)
print(result)