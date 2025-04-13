from collections import deque

dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
N, M, start_y, start_x, start_dir = map(int, input().split())
matrix = [input().split() for _ in range(N)]

visited = [[[False]*4 for _ in range(M)] for __ in range(N)]
que = deque()
que.append((start_y, start_x, start_dir, []))
visited[start_y][start_x][start_dir] = True

result = None

while que:
    now_y, now_x, now_dir, now_route = que.popleft()

    # 현재 방향으로 한 칸 앞에 'X'가 있는지 확인
    dy, dx = dirs[now_dir]
    ny, nx = now_y + dy, now_x + dx
    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 'X':
        result = now_route + ['F']
        break

    # 회전: 왼쪽
    new_d = (now_dir - 1) % 4
    if not visited[now_y][now_x][new_d]:
        visited[now_y][now_x][new_d] = True
        que.append((now_y, now_x, new_d, now_route + ['L']))

    # 회전: 오른쪽
    new_d = (now_dir + 1) % 4
    if not visited[now_y][now_x][new_d]:
        visited[now_y][now_x][new_d] = True
        que.append((now_y, now_x, new_d, now_route + ['R']))

    # 전진: 앞으로 이동
    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 'G':
        if not visited[ny][nx][now_dir]:
            visited[ny][nx][now_dir] = True
            que.append((ny, nx, now_dir, now_route + ['A']))

# 출력
if result:
    print("명령:", ''.join(result))
else:
    print("불가")
