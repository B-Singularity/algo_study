import heapq


def dijkstra(n, graph):
    INF = float('inf')
    distance = [INF] * (n + 1)
    distance[0] = 0

    pq = [(0, 0)]

    while pq:
        current_dist, current_node = heapq.heappop(pq)

        if current_dist > distance[current_node]:
            continue

        for adj_node, weight in graph.get(current_node, []):
            new_dist = current_dist + weight

            if new_dist < distance[adj_node]:
                distance[adj_node] = new_dist
                heapq.heappush(pq, (new_dist, adj_node))

    return distance


T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    Edges = [list(map(int, input().split())) for _ in range(E)]

    graph = {}
    for edge in Edges:
        graph.setdefault(edge[0], []).append((edge[1], edge[2]))

    result = dijkstra(N, graph)[N]
    print(f'#{t} {result}')
