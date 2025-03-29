import heapq

def prim(V, adj):
    visited = [False] * (V + 1)
    pq = [(0, 0)]
    total_weight = 0
    count = 0

    while pq:
        w, u = heapq.heappop(pq)

        if visited[u]:
            continue

        visited[u] = True
        total_weight += w
        count += 1

        if count == V + 1:
            break
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))
    return total_weight


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v, w = edges[i]
        adj[u].append((v, w))
        adj[v].append((u, w))

    result = prim(V, adj)
    print(f'#{t} {result}')