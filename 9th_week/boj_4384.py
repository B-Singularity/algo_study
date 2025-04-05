import sys
input = sys.stdin.readline

N = int(input())
weights = [int(input()) for _ in range(N)]
total = sum(weights)


dp = [0] * (N + 1)
dp[0] = 1

for w in weights:
    for c in range(N, 0, -1):
        dp[c] |= dp[c-1] << w

candidates = [N//2]
if N % 2 == 1:
    candidates.append(N//2 + 1)

best_diff = 10**18
ans = (0, total)

for c in candidates:
    bitset = dp[c]
    mid = total // 2


    for delta in range(mid+1):
        for j in (mid - delta, mid + delta):
            if 0 <= j <= total and ((bitset >> j) & 1):
                diff = abs((total - j) - j)
                if diff < best_diff:
                    best_diff = diff
                    ans = (min(j, total-j), max(j, total-j))
                break
        else:
            continue
        break

print(ans[0], ans[1])
