T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    items = [list(map(int, input().split())) for _ in range(N)]

    dp = [0] * (K + 1)

    for v, c in items:
        for j in range(K, v - 1, -1):
            dp[j] = max(dp[j], dp[j - v] + c)

    print(f'#{t} {dp[K]}')


