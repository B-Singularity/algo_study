from collections import deque

def find_start(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 2:
                return i, j


for _ in range(10):
    t = int(input())
    matrix = [list(map(int, list(input().strip()))) for _ in range(16)]
    start_y, start_x = find_start(matrix)
    que = deque()
    que.append((start_y, start_x, [(start_y, start_x)]))
    visited = [[False] * 16 for _ in range(16)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    flag = False
    route = []
    while que:
        y, x, now_route = que.popleft()
        if matrix[y][x] == 3:
            flag = True
            route = now_route
            break

        visited[y][x] = True
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < 16 and 0 <= nx < 16 and matrix[ny][nx] != 1 and not visited[ny][nx]:
                que.append((ny, nx, now_route + [(ny, nx)]))
    print(f"#{t} {route}")
    print(f'#{t} {1 if flag else 0}')
