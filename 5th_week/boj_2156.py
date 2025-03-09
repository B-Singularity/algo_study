N = int(input())
wine = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N == 1:
    dp[1] = wine[1]
    print(dp[1])
elif N == 2:
    dp[1] = wine[1]
    dp[2] = wine[2] + dp[1]
    print(dp[2])
else:
    dp[1] = wine[1]
    dp[2] = wine[2] + dp[1]
    for i in range(3, N + 1):
        dp[i] = max(dp[i-1], dp[i-2] + wine[i], dp[i-3] + wine[i-1] + wine[i])

    print(max(dp))

