T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [1] * N  # dp[i]: arr[i]를 마지막 원소로 하는 LIS의 길이

    for i in range(N):
        for j in range(i):
            if arr[j] <= arr[i]:  # 증가하는 수열 조건
                dp[i] = max(dp[i], dp[j] + 1)

    print(f'#{t} {max(dp)}')