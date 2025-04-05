N, K = map(int, input().split())
stuffs = [list(map(int, input().split())) for _ in range(N)]
max_value = -1

dp = [0] * (K + 1)

for weight, value in stuffs:
    for j in range(K, weight - 1, -1):
        dp[j] = max(dp[j], dp[j - weight] + value)

print(dp[K])