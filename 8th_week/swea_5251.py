import heapq


def dijkstra(N, edges, start=0):
    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, v = heapq.heappop(pq)
        if dist[v] < d:
            continue
        for to, w in edges[v]:
            cost = dist[v] + w
            if cost < dist[to]:
                dist[to] = cost
                heapq.heappush(pq, (cost, to))

    return dist


T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    edges = [[] for _ in range(N + 1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        edges[u].append((v, w))

    dist = dijkstra(N, edges, start=0)
    print(f'#{t} {dist[N]}')
