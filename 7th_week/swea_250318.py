def recur(arr, visited, depth, total, N, max_value):

    if max_value >= total:
        return max_value

    if depth == N:
        return total

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            max_value = max(max_value, recur(arr, visited, depth + 1, total * (arr[depth][i] * 0.01), N, max_value))
            visited[i] = False

    return max_value

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    possibility = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    max_value = 0
    max_value = recur(possibility, visited, 0, 1, N, max_value) * 100
    max_value = round(max_value, 6)
    print(f'# {max_value:.6f} ')