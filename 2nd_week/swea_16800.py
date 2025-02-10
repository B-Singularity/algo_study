def get_divisor(n):
    result = []
    div = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            result.append(i)
            if n % i != i:
                result.append(n // i)
    for num in result:
        div.append((num, n // num))

    return div



T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = float('inf')
    arr = get_divisor(N)
    for num in arr:
        if result > abs(1 - num[0]) + abs(1 - num[1]):
            result = abs(1 - num[0]) + abs(1 - num[1])

    print(f'#{t} {result}')