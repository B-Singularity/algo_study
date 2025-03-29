def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    jump = [[] for _ in range(K + 1)]
    for i in range(N):
        for j in range(N):
            jump[matrix[i][j]].append((i, j))

    if not jump[1] or any(not jump[i] for i in range(1, K + 1)):
        print(f'#{t} -1')
        continue

    dp = [[] for _ in range(K + 1)]
    dp[1] = [0] * len(jump[1])

    for color in range(2, K + 1):
        dp[color] = [float('inf')] * len(jump[color])
        for cur_idx, cur_pos in enumerate(jump[color]):
            for prev_idx, prev_pos in enumerate(jump[color - 1]):
                cost = dp[color - 1][prev_idx] + get_distance(cur_pos, prev_pos)
                dp[color][cur_idx] = min(dp[color][cur_idx], cost)

    result = min(dp[K])
    print(f'#{t} {result}')



