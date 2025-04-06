INF = int(1e9)
T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for _ in range(M):
        u, v, w = map(int, input().split())
        dist[u][v] = w

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    min_cycle = INF
    for i in range(1, N + 1):
        if dist[i][i] < min_cycle:
            min_cycle = dist[i][i]

    print(f'#{t} {min_cycle if min_cycle != INF else -1}')


