import heapq


def dijkstra(N, K):
    MAX = 100001
    dist = [float('inf')] * MAX
    dist[N] = 0

    pq = []
    heapq.heappush(pq, (0, N))

    while pq:
        current_time, current_pos = heapq.heappop(pq)

        if current_pos == K:
            return current_time

        if current_pos - 1 >= 0 and dist[current_pos - 1] > current_time + 1:
            dist[current_pos - 1] = current_time + 1
            heapq.heappush(pq, (current_time + 1, current_pos - 1))

        if current_pos + 1 < MAX and dist[current_pos + 1] > current_time + 1:
            dist[current_pos + 1] = current_time + 1
            heapq.heappush(pq, (current_time + 1, current_pos + 1))

        if current_pos * 2 < MAX and dist[current_pos * 2] > current_time:
            dist[current_pos * 2] = current_time
            heapq.heappush(pq, (current_time, current_pos * 2))

    return -1


# 입력 받기
N, K = map(int, input().split())

# 다익스트라 함수 실행
result = dijkstra(N, K)

# 결과 출력
print(result)
