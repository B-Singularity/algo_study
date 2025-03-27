import copy
import sys
from collections import deque
input = sys.stdin.readline

def dfs(matrix, visited):
    N = len(matrix)
    M = len(matrix[0])
    island = copy.deepcopy(matrix)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    island_num = 2

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and island[i][j] == 1:
                stack = deque()
                stack.append((i, j))
                visited[i][j] = True
                island[i][j] = island_num
                while stack:
                    y, x = stack.pop()
                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]
                        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and island[ny][nx] == 1:
                            visited[ny][nx] = True
                            island[ny][nx] = island_num
                            stack.append((ny, nx))
                island_num += 1
    return island, island_num

def get_bridges(matrix):
    N = len(matrix)
    M = len(matrix[0])
    bridges = {}
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 1:
                island_id = matrix[i][j]
                for d in range(4):
                    length = 0
                    ny, nx = i, j
                    while True:
                        ny += dy[d]
                        nx += dx[d]
                        if not (0 <= ny < N and 0 <= nx < M):
                            break
                        if matrix[ny][nx] == island_id:
                            break
                        if matrix[ny][nx] == 0:
                            length += 1
                            continue
                        if matrix[ny][nx] != island_id:
                            if length >= 2:
                                other_id = matrix[ny][nx]
                                key = tuple(sorted((island_id, other_id)))
                                if key in bridges:
                                    bridges[key] = min(bridges[key], length)
                                else:
                                    bridges[key] = length
                            break
    edge_list = [(u, v, w) for (u, v), w in bridges.items()]
    return edge_list

def find(node, parent):
    if parent[node] != node:
        parent[node] = find(parent[node], parent)
    return parent[node]

def union(a, b, parent, rank):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a != root_b:
        if rank[root_a] > rank[root_b]:
            parent[root_b] = root_a
        elif rank[root_a] < rank[root_b]:
            parent[root_a] = root_b
        else:
            parent[root_a] = root_b
            rank[root_b] += 1

def kruskal(edges, parent, rank):
    total_weight = 0
    mst = []
    edges.sort(key=lambda x: x[2])
    for u, v, w in edges:
        # 섬 번호를 0부터 시작하는 인덱스로 변환 (섬 번호 - 2)
        u_idx = u - 2
        v_idx = v - 2
        if find(u_idx, parent) != find(v_idx, parent):
            union(u_idx, v_idx, parent, rank)
            mst.append((u, v, w))
            total_weight += w
    return mst, total_weight

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

island, island_num = dfs(matrix, visited)
island_count = island_num - 2

edges = get_bridges(island)

parent = [i for i in range(island_count)]
rank = [0 for _ in range(island_count)]

mst, total_weight = kruskal(edges, parent, rank)

if len(mst) != island_count - 1:
    print(-1)
else:
    print(total_weight)
