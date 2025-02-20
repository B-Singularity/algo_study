def find_start(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 2:
                return i, j


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    start_y, start_x = find_start(maze)

    que = [[start_y, start_x, 1]]
    visited = [[False] * N for _ in range(N)]
    result = 0
    while que:
        y, x, cnt = que.pop(0)
        visited[y][x] = True
        if maze[y][x] == 3:
            result = cnt - 2
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] in (0, 3) and not visited[ny][nx]:
                que.append([ny, nx, cnt + 1])

    print(f'#{t} {result}')




