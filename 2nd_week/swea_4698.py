def prime(n, D):
    prime = [True] * (n + 1)
    cnt = 0
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    for i in range(2, n + 1):
        if prime[i] and str(D) in str(i):
            cnt += 1
    return cnt

T = int(input())
for t in range(1, T + 1):
    D, A, B = map(int, input().split())
    print(f'#{t} {prime(B, D) - prime(A - 1, D)}')
