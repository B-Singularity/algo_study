def dfs(node, depth):
    global max_length
    max_length = max(max_length, depth)

    for next_node in adj[node]:
        if not visited[next_node]:  # 방문하지 않은 정점만 탐색
            visited[next_node] = True
            dfs(next_node, depth + 1)
            visited[next_node] = False  # 백트래킹


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())

    # 인접 리스트 생성
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)

    # 최장 경로 찾기
    max_length = 1
    for i in range(1, N + 1):
        visited = [False] * (N + 1)
        visited[i] = True
        dfs(i, 1)

    print(f'#{t} {max_length}')
