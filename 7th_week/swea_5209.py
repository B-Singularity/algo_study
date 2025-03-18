def recur(arr, depth, total, N, visited, min_value):

    if total >= min_value:
        return min_value

    if depth == N:
        return total

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            min_value = min(min_value, recur(arr, depth + 1, total + arr[depth][i], N, visited, min_value))
            visited[i] = False

    return min_value



T = int(input())
for t in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    result = float('inf')
    visited = [False] * N

    result = recur(V, 0, 0, N, visited, result)

    print(f'#{t} {result}')



