from collections import deque

def turn(now_direction, y, x, operation, N, matrix):
    if operation == 'L':
        now_direction = (now_direction - 1) % 4
    elif operation == 'R':
        now_direction = (now_direction + 1) % 4

    ny, nx = y, x
    if operation == 'A':
        if now_direction == 0:
            ny = y - 1; nx = x
        elif now_direction == 1:
            ny = y;     nx = x + 1
        elif now_direction == 2:
            ny = y + 1; nx = x
        elif now_direction == 3:
            ny = y;     nx = x - 1

        if not (0 <= ny < N and 0 <= nx < N) or matrix[ny][nx] == 'T':
            ny, nx = y, x

    return now_direction, ny, nx

def find_start_and_goal(matrix):
    N = len(matrix)
    start = goal = None
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 'X':
                start = (i, j)
            elif matrix[i][j] == 'Y':
                goal = (i, j)
    return start, goal

T = int(input())
for t in range(1, T + 1):
    N = int(input().strip())
    matrix = [list(input().strip()) for _ in range(N)]
    Q = int(input().strip())
    commands = []
    routes = []
    for _ in range(Q):
        _, cmd = input().split()
        commands.append(cmd)

    (start_y, start_x), (goal_y, goal_x) = find_start_and_goal(matrix)
    result = []

    for cmd in commands:
        now_y, now_x = start_y, start_x
        now_direction = 0
        path = [(now_y, now_x)]

        for op in cmd:
            now_direction, now_y, now_x = turn(now_direction, now_y, now_x, op, N, matrix)
            path.append((now_y, now_x))

        routes.append(path)
        result.append('1' if (now_y, now_x) == (goal_y, goal_x) else '0')


    print(f"#{t} {' '.join(result)}")
    print(routes)
