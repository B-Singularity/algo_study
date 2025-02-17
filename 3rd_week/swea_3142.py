T = int(input())
for t in range(1, T + 1):
    n, m = map(int, input().split())
    a = n - m
    b = 2 * m - n
    print(f'#{t} {b} {a}')