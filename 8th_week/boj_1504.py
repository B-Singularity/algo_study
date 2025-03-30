import sys
import heapq

input = sys.stdin.readline


# 다익스트라 알고리즘
def dijkstra(N, start, adj):
    INF = float('inf')
    dist = [INF] * (N + 1)
    pq = [(0, start)]
    dist[start] = 0

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue

        for v, w in adj[u]:
            new_dist = current_dist + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(pq, (new_dist, v))

    return dist


# 입력 받기
N, E = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))
    adj[v].append((u, w))

v1, v2 = map(int, input().split())

# 다익스트라로 각 경로의 최단 거리 구하기
dist_from_1 = dijkstra(N, 1, adj)
dist_from_v1 = dijkstra(N, v1, adj)
dist_from_v2 = dijkstra(N, v2, adj)

# 두 가지 경로 길이 계산
path1 = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[N]  # 1 -> v1 -> v2 -> N
path2 = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[N]  # 1 -> v2 -> v1 -> N

# 경로가 없으면 -1 출력, 그렇지 않으면 두 경로 중 최소값 출력
result = min(path1, path2)
if result >= float('inf'):
    print(-1)
else:
    print(result)
