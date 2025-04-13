from collections import deque

# 4방향: 0=아래,1=오른쪽,2=위,3=왼쪽
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

N, M, start_y, start_x, start_dir = map(int, input().split())
matrix = [input().split() for _ in range(N)]

# visited[y][x][dir]
visited = [[[False]*4 for _ in range(M)] for __ in range(N)]
que = deque()
# (y, x, dir, 명령 시퀀스 리스트)
que.append((start_y, start_x, start_dir, []))
visited[start_y][start_x][start_dir] = True

result = None  # 경로가 발견되면 저장될 변수

while que:
    y, x, d, route = que.popleft()

    # 적 포탑 'X'가 현재 방향으로 한 칸 앞에 있으면 사격
    dy, dx = dirs[d]
    ny, nx = y + dy, x + dx
    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 'X':
        result = route + ['F']
        break

    # 1) 회전: Left
    nd = (d - 1) % 4
    if not visited[y][x][nd]:
        visited[y][x][nd] = True
        que.append((y, x, nd, route + ['L']))

    # 2) 회전: Right
    nd = (d + 1) % 4
    if not visited[y][x][nd]:
        visited[y][x][nd] = True
        que.append((y, x, nd, route + ['R']))

    # 3) 전진: Advance
    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 'G':
        if not visited[ny][nx][d]:
            visited[ny][nx][d] = True
            que.append((ny, nx, d, route + ['A']))

# 출력
if result:
    print("명령:", ''.join(result))
else:
    print("불가")
