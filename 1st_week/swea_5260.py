T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    dp = [0] * (K + 1)
    dp[0] = 1
    for num in range(1, N + 1):
        for s in range(K, num - 1, -1):
            dp[s] += dp[s - num]

    print(f'#{t} {dp[K]}')