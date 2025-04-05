import sys
input = sys.stdin.readline

C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]

MAX_COST = 100 * C + 1  # worst case: 100 * 1000
dp = [float('inf')] * (MAX_COST)
dp[0] = 0

for cost, gain in cities:
    for i in range(gain, MAX_COST):
        dp[i] = min(dp[i], dp[i - gain] + cost)

print(min(dp[C:]))
