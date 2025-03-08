
N = int(input())  # 집 개수
cost = [list(map(int, input().split())) for _ in range(N)]  # 비용 리스트

# DP 테이블 초기화
dp = [[0] * 3 for _ in range(N+1)]
dp[0] = cost[0]  # 첫 번째 집은 비용 그대로 사용

# DP 계산
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

# 최소 비용 출력
print(min(dp[N-1]))
