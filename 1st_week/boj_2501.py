def divisor(n):
    div = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)
    return sorted(div)

N, K = map(int, input().split())
div = divisor(N)

if K <= len(div):
    print(div[K - 1])
else:
    print(0)

