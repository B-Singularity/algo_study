def find(a, parent):
    if a != parent[a]:
        parent[a] = find(parent[a], parent)
    return parent[a]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    elif rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    else:
        parent[root_a] = root_b
        rank[root_b] += 1



T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)
    edges = []
    flight = [list(map(int, input().split())) for _ in range(M)]
    for fl in flight:
        a, b = fl
        edges.append((a, b))

    cnt = 0
    for a, b in edges:
        if find(a, parent) != find(b, parent):
            union(a, b, parent, rank)
            cnt += 1
    print(cnt)
