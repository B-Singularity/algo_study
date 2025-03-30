import sys
import heapq

input = sys.stdin.readline

def dijkstra(V, K, graph):
    INF = float('inf')
    dist = [INF] * (V + 1)
    dist[K] = 0
    pq = [(0, K)]  # (가중치, 정점)

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, w in graph[u]:
            new_dist = current_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


V, E = map(int, input().split())
K = int(input())  # 시작 정점
graph = [[] for _ in range(V + 1)]  # 인접 리스트로 그래프 구성

# 간선 정보 입력
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 실행
dist = dijkstra(V, K, graph)

# 출력
for i in range(1, V + 1):
    if dist[i] == float('inf'):
        print("INF")
    else:
        print(dist[i])