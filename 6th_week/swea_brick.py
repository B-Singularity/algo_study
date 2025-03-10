import copy
from collections import deque

def update_block(arr):
    H = len(arr)
    W = len(arr[0])
    for i in range(W):
        block = []
        for j in range(H):
            if arr[j][i] != 0:
                block.append(arr[j][i])
                arr[j][i] = 0
        row = H - 1
        while block:
            arr[row][i] = block.pop()
            row -= 1
    return arr

def cnt_block(arr):
    cnt = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != 0:
               cnt += 1
    return cnt

def drop_ball(arr, col):
    H = len(arr)
    W = len(arr[0])
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    deq = deque()
    for i in range(len(arr)):
        if arr[i][col] != 0:
            value = arr[i][col]
            deq.append((i, col, value))
            arr[i][col] = 0
            break
    while deq:
        now_y, now_x, now_value = deq.popleft()
        for pow in range(1, now_value):
            for i in range(4):
                new_y = now_y + dy[i] * pow
                new_x = now_x + dx[i] * pow
                if new_x >= W or new_x < 0 or new_y >= H or new_y < 0:
                    continue
                if arr[new_y][new_x] == 0:
                    continue
                new_value = arr[new_y][new_x]

                deq.append((new_y, new_x, new_value))
                arr[new_y][new_x] = 0
    return arr



def shoot(arr, cnt, N):
    if cnt == N:
        return cnt_block(arr)
    min_value = 301
    arr = update_block(arr)
    for i in range(len(arr[0])):
        temp = copy.deepcopy(arr)
        temp = drop_ball(temp, i)
        temp = update_block(temp)
        min_value = min(min_value, shoot(temp, cnt + 1, N))
    return min_value




T = int(input())
for t in range(1, T + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    result = shoot(board, 0, N)
    print(f'#{t} {result}')
