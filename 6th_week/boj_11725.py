def dfs(current, adjs, visited, result):
    for adj in adjs[current]:
        if not visited[adj]:
            result[adj] = current
            visited[adj] = True
            dfs(adj, adjs, visited, result)


N = int(input())
adj = [[] for _ in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(N - 1)]
for i in range(N - 1):
    a, b = edges[i]
    adj[a].append(b)
    adj[b].append(a)
visited = [False] * (N + 1)
result = [0] * (N + 1)

dfs(1, adj, visited, result)

for i in range(2, N + 1):
    print(result[i])