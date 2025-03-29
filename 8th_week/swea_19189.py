T = int(input())
for t in range(1, T + 1):
    N, P = map(int, input().split())
    # ((N - k + 1) ** 2 )* k! * (N - k)!
    fact = [1] * (N + 1)
    for i in range(1, N + 1):
        fact[i] = (fact[i - 1] * i) % P

    result = 0
    for k in range(1, N + 1):
        term = ((N - k + 1) ** 2) % P
        term = (term * fact[k]) % P
        term = (term * fact[N - k]) % P
        result = (result + term) % P

    print(f'#{t} {result}')
