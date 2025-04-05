import sys
input = sys.stdin.readline

N, M = map(int, input().split())
items = []

for _ in range(N):
    V, C, K = map(int, input().split())
    cnt = 1
    while K > 0:
        use = min(cnt, K)
        items.append((V * use, C * use))
        K -= use
        cnt <<= 1

dp = [0] * (M + 1)
for w, val in items:
    for j in range(M, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + val)

print(dp[M])