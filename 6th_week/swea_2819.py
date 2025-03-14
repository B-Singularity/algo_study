def dfs(arr, cache, current, cnt, y, x):
    if cnt == 6:
        num_tuple = tuple(current)
        if num_tuple not in cache:
            cache.add(num_tuple)
            return 1
        return 0
    result = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        if 0 <= new_y < len(arr) and 0 <= new_x < len(arr[0]):
            current.append(arr[new_y][new_x])
            result += dfs(arr, cache, current, cnt + 1, new_y, new_x)
            current.pop()
    return result

T = int(input())
for t in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(4)]
    cache = set()
    result = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result += dfs(matrix, cache, [matrix[i][j]], 0, i, j)
    print(f'#{t} {result}')
