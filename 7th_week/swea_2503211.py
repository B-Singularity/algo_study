def get_weight(x1, x2, y1, y2, tax):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) * tax



def find(a, parent):
    if parent[a] != a:
        parent[a] = find(parent[a], parent)
    return parent[a]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if rank[root_b] > rank[root_a]:
        parent[root_a] = root_b
    elif rank[root_b] < rank[root_a]:
        parent[root_b] = root_a
    else:
        parent[root_b] = root_a
        rank[root_a] += 1


def kruskal(edges, parent, rank):
    edges.sort()
    mst = []
    total_weight = 0

    for weight, u, v in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            mst.append((u, v, weight))
            total_weight += weight

    return total_weight




T = int(input())
for t in range(1, T + 1):
    N = int(input())
    edges = []
    x_cordinates = list(map(int, input().split()))
    y_cordinates = list(map(int, input().split()))
    parent = [i for i in range(N)]
    rank = [0 for i in range(N)]
    tax = float(input())
    for i in range(N - 1):
        for j in range(i + 1, N):
            edges.append([get_weight(x_cordinates[i], x_cordinates[j], y_cordinates[i], y_cordinates[j], tax), i, j])
    print(f'#{t} {round(kruskal(edges, parent, rank))}')

