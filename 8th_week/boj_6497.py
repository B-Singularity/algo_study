import sys

input = sys.stdin.readline


def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]


def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a
            rank[root_a] += 1


def kruskal(edges, parent, rank):
    mst = []
    total_weight = 0
    edges.sort(key=lambda x: x[2])
    for u, v, weight in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    edges = [list(map(int, input().split())) for _ in range(n)]
    total_weight_all = sum(edge[2] for edge in edges)

    parent = [i for i in range(m)]
    rank = [0 for _ in range(m)]

    mst, total_weight = kruskal(edges, parent, rank)
    result = total_weight_all - total_weight
    print(result)



