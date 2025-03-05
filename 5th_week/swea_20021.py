def get_primes(num):
    primes = [True] * (num + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(num ** (1/2)) + 1):
        if primes[i]:
            for j in range(i * i, num + 1, i):
                primes[j] = False
    return [i for i in range(2, num + 1) if primes[i]]

T = int(input())
for t in range(1, T + 1):
    n = int(input())
    primes = get_primes((n ** 2 - n) // 2)
    # 간선 모두 더해서 2로 나눔 -> 소수

    # 0 1 1 0 1   4
    # 0 0 1 0 0   3
    # 0 0 0 1 1   2
    # 0 0 0 0 1   1
    # 0 0 0 0 0

    # 개수는 n ** 2 - n // 2
    # n = 5, 25 - 5 // 2 == 10