def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)

    x = y1
    y = x1 - (a // b) * y1

T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    print(f'#{t} {extended_gcd(A, B)}')