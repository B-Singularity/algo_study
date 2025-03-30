import sys
import math
import heapq

input = sys.stdin.readline

def get_distance(a, b):
    """ 두 별 사이의 유클리드 거리 계산 """
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def prim(N, stars):
    """ PRIM 알고리즘을 이용한 최소 신장 트리 (MST) """
    total_weight = 0
    pq = [(0, 0)]  # (거리, 시작 노드)
    visited = [False] * N
    cnt = 0

    while pq:
        w, u = heapq.heappop(pq)
        if visited[u]:  # 이미 방문한 노드는 스킵
            continue
        visited[u] = True
        total_weight += w
        cnt += 1

        if cnt == N:  # 모든 별이 연결되면 종료
            break

        for v in range(N):
            if not visited[v] and u != v:
                heapq.heappush(pq, (get_distance(stars[u], stars[v]), v))

    return round(total_weight, 2)  # 소수점 둘째 자리까지 출력

# 입력 처리
N = int(input())
stars = [tuple(map(float, input().split())) for _ in range(N)]

# 최소 비용 출력
print(prim(N, stars))
