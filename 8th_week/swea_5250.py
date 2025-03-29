import heapq

from sympy.codegen.rewriting import matinv_opt


def djikstra(N, matrix):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = 0

    pq = [(0, 0, 0)]

    while pq:
        d, y, x = heapq.heappop(pq)

        if dist[y][x] < d:
            continue

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                needed = max(0, matrix[ny][nx] - matrix[y][x])
                nd = needed + 1 + d

                if nd < dist[ny][nx]:
                    dist[ny][nx] = nd
                    heapq.heappush(pq, (nd, ny, nx))


    return dist

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    dist = djikstra(N, matrix)
    print(f'#{t} {dist[N - 1][N - 1]}')

