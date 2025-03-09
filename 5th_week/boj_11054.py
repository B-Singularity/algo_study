N = int(input())
A = list(map(int, input().split()))
reversed_A = list(reversed(A))
dp_A = [1] * N
dp_reversed_A = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_A[i] = max(dp_A[i], dp_A[j] + 1)
        if reversed_A[i] > reversed_A[j]:
            dp_reversed_A[i] = max(dp_reversed_A[i], dp_reversed_A[j] + 1)

result = 0
for i in range(N):
    result = max(result, dp_A[i] + dp_reversed_A[N - i - 1] - 1)
print(result)

