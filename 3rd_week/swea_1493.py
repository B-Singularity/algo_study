T = int(input())
for t in range(T):
    p, q = map(int, input().split())

    n1 = 1
    while (n1 * (n1 - 1)) // 2 + 1 <= p:
        n1 += 1
    n1 -= 1
    x1 = p - (n1 * (n1 - 1)) // 2
    y1 = (n1 + 1) - x1

    n2 = 1
    while (n2 * (n2 - 1)) // 2 + 1 <= q:
        n2 += 1
    n2 -= 1
    x2 = q - (n2 * (n2 - 1)) // 2
    y2 = (n2 + 1) - x2

    result_x = x1 + x2
    result_y = y1 + y2

    result_n = result_x + result_y - 1
    result_value = (result_n * (result_n - 1)) // 2 + result_x

    print(f'#{t + 1} {result_value}')


