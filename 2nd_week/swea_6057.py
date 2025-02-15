from itertools import combinations

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    edges = {}

    for _ in range(M):
        x, y = map(int, input().split())
        edges.setdefault(x, []).append(y)
        edges.setdefault(y, []).append(x)

    comb = combinations(edges.keys(), 3)
    cnt = 0

    for c in comb:
        a, b, c = c
        if b in edges.get(a, []) and c in edges.get(b, []) and a in edges.get(c, []):
            cnt += 1

    print(f'#{t} {cnt}')
