import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    last_rank = list(map(int, input().split()))
    m = int(input())
    changed_rank = [list(map(int, input().split())) for _ in range(m)]
    adj = [[False] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(n):
        for j in range(i + 1, n):
            adj[last_rank[i]][last_rank[j]] = True
            indegree[last_rank[j]] += 1

    for a, b in changed_rank:
        if adj[a][b]:
            adj[a][b] = False
            adj[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            adj[b][a] = False
            adj[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    q = deque()
    result = []
    flag = True

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(n):
        if not q:
            print("IMPOSSIBLE")
            flag = False
            break

        if len(q) > 1:
            print("?")
            flag = False
            break
        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            if adj[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if flag:
        print(" ".join(map(str, result)))


