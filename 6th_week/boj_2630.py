def check(arr, y_start, y_end, x_start, x_end):
    first = arr[y_start][x_start]
    for i in range(y_start, y_end):
        for j in range(x_start, x_end):
            if arr[i][j] != first:
                return False
    return True


def recur(arr, y_start, y_end, x_start, x_end):
    if check(arr, y_start, y_end, x_start, x_end):
        if arr[y_start][x_start] == 0:
            return 1, 0
        else:
            return 0, 1

    mid_y = (y_start + y_end) // 2
    mid_x = (x_start + x_end) // 2
    white1, blue1 = recur(arr, y_start, mid_y, x_start, mid_x)  # 왼쪽 상단
    white2, blue2 = recur(arr, y_start, mid_y, mid_x, x_end)    # 오른쪽 상단
    white3, blue3 = recur(arr, mid_y, y_end, x_start, mid_x)    # 왼쪽 하단
    white4, blue4 = recur(arr, mid_y, y_end, mid_x, x_end)
    return white1 + white2 + white3 + white4, blue1 + blue2 + blue3 + blue4

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = recur(arr, 0, N, 0, N)
print(cnt[0])
print(cnt[1])

