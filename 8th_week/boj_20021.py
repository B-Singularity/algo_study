def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime


prime_sieve = sieve(1000 * 999 // 2)


T = int(input())
for t in range(1, T + 1):
    n = int(input())
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1))
    edges.append((n, 1))

    degree = [0] * (n + 1)
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1

    extra = 0
    while not prime_sieve[len(edges) + extra]:
        extra += 1

    needed = extra
    i = 1
    while needed > 0 and i <= n:
        j = i + 2
        if j > n:
            j -= n
        if degree[i] == 2 and degree[j] == 2:
            a, b = min(i, j), max(i, j)
            edges.append((a, b))
            degree[i] += 1
            degree[j] += 1
            needed -= 1
        i += 1

    if needed != 0:
        print(-1)
    else:
        print(len(edges))
        for u, v in edges:
            print(u, v)



