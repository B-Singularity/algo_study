import sys
import math


def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]


def union(x, y, parent, rank):
    xroot = find(x, parent)
    yroot = find(y, parent)
    if xroot != yroot:
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


def get_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def main():
    input = sys.stdin.readline
    N, M = map(int, input().split())

    # 우주신들의 좌표 입력 (황선자 포함)
    coords = [tuple(map(int, input().split())) for _ in range(N)]

    # Union-Find 초기화
    parent = [i for i in range(N)]
    rank = [0] * N

    # 이미 연결된 통로들 먼저 연결 (0-based 인덱스)
    for _ in range(M):
        u, v = map(int, input().split())
        union(u - 1, v - 1, parent, rank)

    # 모든 가능한 간선 (우주신 간의 거리) 생성
    edges = []
    for i in range(N):
        for j in range(i + 1, N):
            d = get_distance(coords[i], coords[j])
            edges.append((d, i, j))

    # 가중치(거리)를 기준으로 정렬
    edges.sort(key=lambda x: x[0])

    total_cost = 0.0
    # 크루스칼 알고리즘 수행
    for d, u, v in edges:
        if find(u, parent) != find(v, parent):
            union(u, v, parent, rank)
            total_cost += d

    # 소수점 둘째 자리까지 반올림하여 출력
    print(f"{total_cost:.2f}")


if __name__ == "__main__":
    main()
