import math
import heapq

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

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


def get_distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x ** 2 + y ** 2)



def kruskal(graph, parent, rank):
    graph.sort(key=lambda x: x[2])
    mst = []
    total_weight = 0

    for u, v, weight in graph:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight

n = int(input())
coordinates = [list(map(float, input().split())) for _ in range(n)]
parent = [i for i in range(n)]
rank = [0 for i in range(n)]
graph = []
for i in range(n - 1):
    for j in range(i + 1, n):
        graph.append([i, j, get_distance(coordinates[i], coordinates[j])])

print(round(kruskal(graph, parent, rank)[1], 2))


