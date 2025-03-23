import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    K = int(input().strip())
    files = list(map(int, input().split()))

    prefix = [0] * (K + 1)
    for i in range(K):
        prefix[i + 1] = prefix[i] + files[i]

    dp = [[0] * (K + 1) for _ in range(K + 1)]
    opt = [[0] * (K + 1) for _ in range(K + 1)]

    for i in range(K):
        dp[i][i] = 0
        opt[i][i] = i

    for length in range(2, K + 1):
        for i in range(K - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')

            start = opt[i][j - 1] if i < j else i
            end = opt[i + 1][j] if i + 1 <= j else j

            for k in range(start, end + 1):
                cost = dp[i][k] + dp[k + 1][j] + (prefix[j + 1] - prefix[i])
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    opt[i][j] = k

    sys.stdout.write(str(dp[0][K - 1]) + "\n")
