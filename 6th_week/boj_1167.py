import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current, adj, visited, total):
    # 현재 노드를 방문 처리하고, 기본값으로 현재 누적 거리와 현재 노드를 저장합니다.
    visited[current] = True
    farthest_distance = total
    farthest_node = current
    # 인접한 모든 노드에 대해 DFS를 진행합니다.
    for nxt in adj.get(current, {}):
        if not visited[nxt]:
            distance, node = dfs(nxt, adj, visited, total + adj[current][nxt])
            # 더 멀리 도달할 수 있다면 값을 갱신합니다.
            if distance > farthest_distance:
                farthest_distance = distance
                farthest_node = node
    return farthest_distance, farthest_node

V = int(input())
adj = dict()

# 입력 형식: 각 줄은 정점번호, (인접정점, 거리) 쌍이 반복되고 -1로 끝남.
for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        neighbor = data[i]
        distance = data[i+1]
        adj.setdefault(node, {})[neighbor] = distance
        i += 2

# 첫 번째 DFS: 임의의 노드(1번)에서 가장 멀리 있는 노드(farthest)를 찾습니다.
visited = [False] * (V + 1)
_, farthest = dfs(1, adj, visited, 0)

# 두 번째 DFS: 찾은 노드(farthest)에서 트리의 지름(최대 거리)을 구합니다.
visited = [False] * (V + 1)
diameter, _ = dfs(farthest, adj, visited, 0)

print(diameter)