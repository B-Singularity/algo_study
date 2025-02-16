T = int(input())
for t in range(1, T + 1):
    N = int(input())
    #fn = fn-2 + fn-3
    dp = [0] * (101)
    dp[1] = dp[2] = dp[3] = 1
    for i in range(4, 101):
        dp[i] = dp[i - 2] + dp[i - 3]
    print(f'#{t} {dp[N]}')