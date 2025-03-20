def find(a, parent):
    if parent[a] != a:
        parent[a] = find(parent[a], parent)
    return parent[a]

def union(x, y, parent, rank):
    rootx = find(x, parent)
    rooty = find(y, parent)

    if rootx != rooty:
        if rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
        else:
            parent[rooty] = rootx
            rank[rootx] += 1

n, m = map(int, input().split())
operations = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]
rank = [0] * (n + 1)

for oper in operations:
    num, a, b = oper
    if num == 1:
        if find(a, parent) == find(b, parent):
            print('YES')
        else:
            print('NO')
    else:
        union(a, b, parent, rank)
