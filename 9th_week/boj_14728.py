N, T = map(int, input().split())
chapters = [map(int, input().split()) for _ in range(N)]
dp = [0] * (T + 1)

for chapter in chapters:
    times, score = chapter
    for i in range(T, times - 1, -1):
        dp[i] = max(dp[i], dp[i - times] + score)
print(dp[T])