N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
if N == 1:
    print(stairs[1])
elif N == 2:
    print(stairs[2] + stairs[1])
else:
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]
    print(dp[N])