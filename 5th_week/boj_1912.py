N = int(input())
numbers = list(map(int, input().split()))

dp = [0] * N
dp[0] = numbers[0]
max_value = dp[0]

for i in range(1, N):
    dp[i] = max(numbers[i], dp[i - 1] + numbers[i])
    max_value = max(max_value, dp[i])

print(max_value)
