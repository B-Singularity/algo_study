import sys
import heapq
input = sys.stdin.readline

def prim(N, adj):
    total_weight = 0
    mst = []
    pq = [(0, 1)]
    visited = [False] * (N + 1)
    cnt = 0

    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_weight += w
        cnt += 1

        if cnt == N:
            break

        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))

    return mst, total_weight

def find(node, parent):
    if node != parent[node]:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(u, v, parent, rank):
    root_u = find(u, parent)
    root_v = find(v, parent)

    if root_u != root_v:
        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

def kruskal(N, E, edges):
    sorted_edges = sorted(edges, key=lambda x : x[2])
    mst = []
    total_weight = 0
    cnt = 0
    parent = [i for i in range(N + 1)]
    rank = [0 for _ in range(N + 1)]



    for u, v, w in sorted_edges:
        if cnt == E:
            break
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            total_weight += w
            mst.append((u, v, w))
            cnt += 1

    return mst, total_weight

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
adj = [[] for _ in range(V + 1)]
for u, v, w in edges:
    adj[u].append((v, w))
    adj[v].append((u, w))

print(kruskal(V, E, edges)[1])
# print(prim(V, adj)[1])

