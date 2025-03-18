T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    N, stations = arr[0], arr[1:] + [0]
    dp = [float('inf')] * N
    dp[0] = 0

    for i in range(N - 1):
        step = stations[i]
        for j in range(1, step + 1):
            if j + i < N:
                dp[i + j] = min(dp[i + j], dp[i] + 1)
    print(f'#{t} {dp[N - 1] - 1}')

