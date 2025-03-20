import heapq

def min_fuel_cost(N, heights):
    INF = float('inf')
    distance = [[INF] * N for _ in range(N)]
    distance[0][0] = 0

    pq = [(0, 0, 0)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        fuel, x, y = heapq.heappop(pq)

        if fuel > distance[x][y]:
            continue

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                additional_fuel = 1

                if heights[nx][ny] > heights[x][y]:
                    additional_fuel += heights[nx][ny] - heights[x][y]

                new_fuel = fuel + additional_fuel

                if new_fuel < distance[nx][ny]:
                    distance[nx][ny] = new_fuel
                    heapq.heappush(pq, (new_fuel, nx, ny))

    return distance[N - 1][N - 1]


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    heights = [list(map(int, input().split())) for _ in range(N)]

    result = min_fuel_cost(N, heights)
    print(f"#{t} {result}")