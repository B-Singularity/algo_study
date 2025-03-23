import sys
import heapq

input = sys.stdin.readline
N = int(input())
que = []
output = []

for _ in range(N):
    num = int(input())
    if num == 0:
        if que:
            output.append(-heapq.heappop(que))
        else:
            output.append(0)
    else:
        heapq.heappush(que, -num)

sys.stdout.write("\n".join(map(str, output)))
