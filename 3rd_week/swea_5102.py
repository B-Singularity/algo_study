T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    result = 0
    que = [[S, 0]]
    visited = [False] * (V + 1)
    while que:
        node, cnt = que.pop(0)
        visited[node] = True
        if node == G:
            result = cnt
            break

        for next_node in graph[node]:
            if not visited[next_node]:
                que.append([next_node, cnt + 1])

    print(f'#{t} {result}')
