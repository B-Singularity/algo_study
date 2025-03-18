def recur(a, b, c):
    if b == 0:
        return 1 % c
    if b % 2 == 0:
        half = recur(a, b // 2, c)
        return (half * half) % c
    else:
        half = recur(a, (b - 1) // 2, c)
        return (a * half * half) % c



A, B, C = map(int, input().split())
result = recur(A, B, C)
print(result)