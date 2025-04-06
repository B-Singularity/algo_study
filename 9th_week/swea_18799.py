T = int(input())
for t in range(1, T + 1):
    n = int(input())
    s = list(map(int, input().split()))

    partial_avg = []
    for i in range(1, 1 << n):
        total = 0
        length = bin(i).count('1')
        for j in range(n):
            if i & (1 << j):
                total += s[j]
        partial_avg.append(total / length)

    result = sum(partial_avg) / len(partial_avg)
    if result == int(result):
        result = int(result)
    print(f'#{t} {round(result, 20)}')

