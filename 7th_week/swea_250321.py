import heapq


def dijkstra(start_y, start_x, matrix, n):
    INF = float('inf')
    distance = [[INF] * n for _ in range(n)]
    distance[start_y][start_x] = int(matrix[start_y][start_x])

    pq = [(int(matrix[start_y][start_x]), start_y, start_x)]

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while pq:
        dist, now_y, now_x = heapq.heappop(pq)

        if distance[now_y][now_x] < dist:
            continue

        for i in range(4):
            new_y = now_y + dy[i]
            new_x = now_x + dx[i]

            if 0 <= new_y < n and 0 <= new_x < n:
                cost = dist + int(matrix[new_y][new_x])

                if cost < distance[new_y][new_x]:
                    distance[new_y][new_x] = cost
                    heapq.heappush(pq, (cost, new_y, new_x))

    return distance[n - 1][n - 1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, list(input().strip()))) for _ in range(N)]
    result = dijkstra(0, 0, matrix, N)
    print(f'#{t} {result}')

