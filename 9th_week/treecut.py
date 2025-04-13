from collections import deque

def find_start(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 'X':
                return i, j

T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(input().strip()) for _ in range(N)]
    sy, sx = find_start(matrix)

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = [[[[False] * (K + 1) for _ in range(4)] for _ in range(N)] for _ in range(N)]
    q = deque()

    visited[sy][sx][0][K] = True
    q.append((sy, sx, 0, 0, K))

    answer = -1

    while q:
        y, x, dir, cnt, cuts = q.popleft()

        if matrix[y][x] == 'Y':
            answer = cnt
            break

        ny, nx = y + dy[dir], x + dx[dir]
        if 0 <= ny < N and 0 <= nx < N:
            cell = matrix[ny][nx]
            if cell in 'GY' and not visited[ny][nx][dir][cuts]:
                visited[ny][nx][dir][cuts] = True
                q.append((ny, nx, dir, cnt + 1, cuts))
            elif cell == 'T' and cuts > 0 and not visited[ny][nx][dir][cuts - 1]:
                visited[ny][nx][dir][cuts - 1] = True
                q.append((ny, nx, dir, cnt + 1, cuts - 1))

        for d in [-1, 1]:
            nd = (dir + d) % 4
            if not visited[y][x][nd][cuts]:
                visited[y][x][nd][cuts] = True
                q.append((y, x, nd, cnt + 1, cuts))

    print(f"#{t} {answer}")
