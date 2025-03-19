def dfs(arr, cur, visited):
    max_length = 1
    for nxt in arr[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            max_length = max(max_length, 1 + dfs(arr, nxt, visited))
            visited[nxt] = False
    return max_length


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(M)]

    arr = [[] for _ in range(N + 1)]
    for edge in edges:
        arr[edge[0]].append(edge[1])
        arr[edge[1]].append(edge[0])


    result = 0


    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True
        result = max(result, dfs(arr, i, visited))

    print(f"#{t} {result}")
