T = int(input())
for t in range(1, T + 1):
    flag = False
    V, E = map(int, input().split())
    adj = {i: [] for i in range(1, V + 1)}
    visited = [False] * (V + 1)

    for _ in range(E):
        start, end = map(int, input().split())
        adj[start].append(end)

    S, G = map(int, input().split())

    stack = [S]
    while stack:
        now_node = stack.pop()
        if now_node == G:
            flag = True
            break
        if not visited[now_node]:
            visited[now_node] = True
            stack.extend(adj[now_node])

    print(f'#{t} {1 if flag else 0}')


