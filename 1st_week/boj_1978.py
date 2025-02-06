def counting_Prime(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if not prime[i]:
            continue
        for j in range(i * i, n + 1, i):
            prime[j] = False
    return prime

N = int(input())
arr = list(map(int, input().split()))
max_num = -1
cnt = 0
for num in arr:
    if max_num < num:
        max_num = num
isPrime = counting_Prime(max_num)
for num in arr:
    if isPrime[num]:
        cnt += 1

print(cnt)
