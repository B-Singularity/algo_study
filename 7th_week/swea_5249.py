import heapq


def prim(n, graph):
    mst = []
    visited = [False] * (n + 1)
    min_heap = [(0, 0)]
    parent = [-1] * (n + 1)

    while min_heap:
        weight, u = heapq.heappop(min_heap)

        if visited[u]:
            continue
        visited[u] = True

        if parent[u] != -1:
            mst.append((parent[u], u, weight))

        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))
                parent[v] = u

    return mst


T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    Edges = [list(map(int, input().split())) for _ in range(E)]
    graph = {}

    for u, v, w in Edges:
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))

    mst = prim(V, graph)
    result = sum(weight for _, _, weight in mst)

    print(f'#{t} {result}')
