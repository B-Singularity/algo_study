import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

que = deque()
for i in range(1, N + 1):
    if indegree[i] == 0:
        que.append(i)

result = []

while que:
    current = que.popleft()
    result.append(current)
    for neighbor in graph[current]:
        indegree[neighbor] -= 1
        if indegree[neighbor] == 0:
            que.append(neighbor)

print(*result)