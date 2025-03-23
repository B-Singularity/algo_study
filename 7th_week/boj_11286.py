import sys
import heapq

input = sys.stdin.readline
n = int(input())
heap = []
result = []

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    else:
        if heap:
            result.append(heapq.heappop(heap)[1])
        else:
            result.append(0)

sys.stdout.write("\n".join(map(str, result)))
