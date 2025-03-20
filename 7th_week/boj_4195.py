def find(a, parent):
    if a != parent[a][0]:
        parent[a][0] = find(parent[a][0], parent)  # 경로 압축
    return parent[a][0]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_b] > rank[root_a]:
            parent[root_a][0] = root_b
            parent[root_b][1] += parent[root_a][1]
        elif rank[root_b] < rank[root_a]:
            parent[root_b][0] = root_a
            parent[root_a][1] += parent[root_b][1]
        else:
            parent[root_a][0] = root_b
            parent[root_b][1] += parent[root_a][1]
            rank[root_b] += 1  # 랭크 증가

    return parent[find(a, parent)][1]  # 최종 집합 크기 반환

T = int(input())
for t in range(1, T + 1):
    F = int(input())
    friends = [input().split() for _ in range(F)]
    parent = {}
    rank = {}

    for friend in friends:
        parent.setdefault(friend[0], [friend[0], 1])
        parent.setdefault(friend[1], [friend[1], 1])
        rank.setdefault(friend[0], 0)
        rank.setdefault(friend[1], 0)

    for friend in friends:
        print(union(friend[0], friend[1], parent, rank))
