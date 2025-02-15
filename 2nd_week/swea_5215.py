T = int(input())
for t in range(1, T + 1):
    N, L = map(int, input().split())
    scores = [list(map(int, input().split())) for _ in range(N)]
    dp = [0] * (L + 1)

    for taste, cal in scores:
        for j in range(L, cal - 1, -1):
            dp[j] = max(dp[j], dp[j - cal] + taste)

    print(f'#{t} {dp[L]}')