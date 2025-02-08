T = int(input())
for t in range(1, T + 1):
    a, b, c = map(int, input().split())

    x1 = round(abs(2 * b - a - c), 1)
    x2 = round(abs(a + c - 2 * b), 1)
    x3 = round(abs((a + c) / 2 - b), 1)
    result = min(x1, x2, x3)
    if result == 0:
        print(f'#{t} 0.0')
    else:
        print(f'#{t} {result}')