for t in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    start_y, start_x = -1, -1
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                start_y, start_x = i, j
                break

    que = [[start_y, start_x]]
    visited = [[False] * 16 for _ in range(16)]
    flag = False

    while que:
        y, x = que.pop()
        visited[y][x] = True
        if matrix[y][x] == 3:
            flag = True
            break
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < 16 and 0 <= nx < 16 and not visited[ny][nx] and matrix[ny][nx] in (0, 3):
                que.append([ny, nx])

    if flag:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')
