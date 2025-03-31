from collections import deque

N, K = map(int, input().split())

dp = [float('inf')] * 100001
prev = [-1] * 100001

queue = deque()
queue.append((N, 0))
dp[N] = 0

while queue:
    now, time = queue.popleft()

    if now == K:
        break

    for next_pos in (now - 1, now + 1, now * 2):
        if 0 <= next_pos < 100001 and dp[next_pos] > time + 1:
            dp[next_pos] = time + 1
            prev[next_pos] = now
            queue.append((next_pos, time + 1))

print(dp[K])

path = []
cur = K
while cur != -1:
    path.append(cur)
    cur = prev[cur]
path.reverse()

print(" ".join(map(str, path)))
