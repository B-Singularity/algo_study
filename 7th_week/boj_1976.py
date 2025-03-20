def find(a, parent):
    if parent[a] != a:
        parent[a] = find(parent[a], parent)
    return parent[a]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_a] = root_b
            rank[root_b] += 1

N = int(input())
M = int(input())
cities = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N + 1)]
rank = [0] * (N + 1)
trip_plan = list(map(int, input().split()))
for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cities[i - 1][j - 1] == 1:
            union(i, j, parent, rank)

p = find(trip_plan[0], parent)
flag = True
for city in trip_plan:
    if p != find(city, parent):
        flag = False
        break

if flag:
    print('YES')
else:
    print('NO')