N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)
for i in range(N):
    weight, value = stuffs[i]
    for j in range(K, stuffs[i][0] - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])