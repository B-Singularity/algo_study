from collections import deque

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

type_dir = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}

# 반대 방향
opp_dir = {0: 1, 1: 0, 2: 3, 3: 2}

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    que = deque()
    que.append((R, C, 1))
    visited[R][C] = True
    cnt = 1

    while que:
        y, x, time = que.popleft()
        if time >= L:
            continue

        curr_type = matrix[y][x]
        for d in type_dir.get(curr_type, []):
            dy, dx = dirs[d]
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
                next_type = matrix[ny][nx]
                if next_type != 0 and opp_dir[d] in type_dir.get(next_type, []):
                    visited[ny][nx] = True
                    que.append((ny, nx, time + 1))
                    cnt += 1

    print(f"#{t} {cnt}")
