prime = [True] * 1000001
prime[0] = prime[1] = False
n = 1000000
for i in range(2, int(n ** (0.5)) + 1):
    if prime[i]:
        for j in range(i * i, n + 1, i):
            prime[j] = False

result = [i for i in range(2, n + 1) if prime[i]]
print(" ".join(map(str, result)))
