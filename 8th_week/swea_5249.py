import heapq

from torch.onnx.symbolic_opset9 import randint_like


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

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        elif rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
            rank[root_b] += 1

def kruskal(V, edges):
    parent = list(range(V + 1))
    rank = [0] * (V + 1)
    mst = []
    total_weight = 0
    edges.sort(key = lambda x : x[2])
    for edge in edges:
        u, v, w = edge
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            mst.append(edge)
            total_weight += w

        if len(mst) == V:
            break

    return total_weight, mst



T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    adj = [[] for _ in range(V + 1)]

    for i in range(E):
        u, v, w = edges[i]
        adj[u].append((v, w))
        adj[v].append((u, w))

    result1 = prim(V, adj)
    result2 = kruskal(V, edges)
    print(f'#{t} {result1}')
    print(f'#{t} {result2}')