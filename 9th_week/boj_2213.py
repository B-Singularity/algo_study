import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n = int(input())
w = [0] + list(map(int, input().split()))

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

dp = [[0, 0] for _ in range(n+1)]
visited = [False] * (n+1)

def dfs(u):
    visited[u] = True
    dp[u][0] = 0
    dp[u][1] = w[u]
    for v in tree[u]:
        if not visited[v]:
            dfs(v)
            dp[u][0] += max(dp[v][0], dp[v][1])
            dp[u][1] += dp[v][0]

dfs(1)

selected = []
visited = [False] * (n+1)

def trace(u, can_take):
    visited[u] = True
    if can_take and dp[u][1] > dp[u][0]:
        selected.append(u)
        for v in tree[u]:
            if not visited[v]:
                trace(v, False)
    else:
        for v in tree[u]:
            if not visited[v]:
                trace(v, True)

trace(1, True)

answer = max(dp[1][0], dp[1][1])
print(answer)
print(*sorted(selected))
