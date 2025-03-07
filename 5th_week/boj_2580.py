def is_valid(board, y, x, num):
    for i in range(9):
        if board[y][i] == num:
            return False
        if board[i][x] == num:
            return False

    start_y = (y // 3) * 3
    start_x = (x // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_y + i][start_x + j] == num:
                return False
    return True

def backtrack(arr):
    # 0인 칸 찾기 -> 1부터 9까지 넣어보기 -> 그 상태로 다른 0에 넣어보기 -> 안 되면 빠꾸치기 -> 다 빠져나왔으면 틀림 복구 ->
    for i in range(9):
        for j in range(9):
            if arr[i][j] == 0:
                for k in range(1, 10):
                    if is_valid(arr, i, j, k):
                        arr[i][j] = k

                        if backtrack(arr):
                            return True

                        arr[i][j] = 0
                return False

    return True




sdoku = [list(map(int, input().split())) for _ in range(9)]
backtrack(sdoku)
for row in sdoku:
    print(' '.join(map(str, row)))

