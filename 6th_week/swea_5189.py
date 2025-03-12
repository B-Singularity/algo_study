def recur(current, visited, N, battery, consumption):
    global min_consumption

    if all(visited):
        consumption += battery[current][0]
        min_consumption = min(min_consumption, consumption)
        return

    if consumption >= min_consumption:
        return

    for next_node in range(N):
        if not visited[next_node]:
            visited[next_node] = True
            recur(next_node, visited, N, battery, consumption + battery[current][next_node])
            visited[next_node] = False

def recur2(current, visited, N, batttery, cnt, current_consumption, best):
    if current_consumption >= best:
        return

    if cnt == N:
        total = current_consumption + batttery[current][0]
        best = min(best, total)
        return total

    min_consumption = float('inf')

    for next_node in range(N):
        if not visited[next_node]:
            visited[next_node] = True
            cost = recur2(next_node, visited, N, batttery, cnt + 1, current_consumption + batttery[current][next_node], best)
            min_consumption = min(min_consumption, cost)
            visited[next_node] = False

    return min_consumption

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    battery = [list(map(int, input().split())) for _ in range(N)]

    min_consumption = float('inf')
    visited = [False] * N
    visited[0] = True
    best = float('inf')
    result = recur2(0, visited, N, battery, 1, 0, best)

    # 결과 출력
    print(f"#{t} {result}")