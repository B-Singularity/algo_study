def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)
    return parent[a]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_b] > rank[root_a]:
            parent[root_a] = root_b
        elif rank[root_b] < rank[root_a]:
            parent[root_b] = root_a
        else:
            parent[root_a] = root_b
            rank[root_b] += 1

def kruskal(edges, parent, rank):
    edges.sort(key=lambda x: x[2])
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
parent = [i for i in range(V + 1)]
rank = [0] * (V + 1)

print(kruskal(edges, parent, rank)[1])
