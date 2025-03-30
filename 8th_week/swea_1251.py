import heapq
import math

def get_distance(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return math.sqrt(x**2 + y**2)

def get_price(L, E):
    return E * (L ** 2)

def find(node, parent):
    if node != parent[node]:
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
            rank[root_a] += 1

def kruskal(N, edges, island, E):
    edges.sort(key=lambda x: x[2])
    total_price = 0
    parent = [i for i in range(N)]
    rank = [0] * N
    cnt = 0

    for u, v, w in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            L = get_distance(island[u], island[v])
            total_price += get_price(L, E)
            cnt += 1
            if cnt == N - 1:
                break
    return round(total_price)

def prim(N, adj, E):
    pq = [(0, 0)]
    total_price = 0
    cnt = 0
    visited = [False] * N

    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]:
            continue
        visited[u] = True
        total_price += get_price(w, E)
        cnt += 1
        if cnt == N:
            break
        for v, w in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
    return round(total_price)






T = int(input())
for t in range(1, T + 1):
    N = int(input())
    x_cor = list(map(int, input().split()))
    y_cor = list(map(int, input().split()))
    E = float(input())
    islands = [(x_cor[i], y_cor[i]) for i in range(N)]
    adj = [[] for _ in range(N)]
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            dist = get_distance(islands[i], islands[j])
            adj[i].append((j, dist))
            adj[j].append((i, dist))
            edges.append((i, j, dist))
    answer = prim(N, adj, E)
    answer2 = kruskal(N, edges, islands, E)
    print(f'#{t} {answer}')
    print(f'#{t} {answer2}')


