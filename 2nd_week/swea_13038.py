T = int(input())

for t in range(1, T + 1):
    n = int(input())
    cl = list(map(int, input().split()))

    count_1 = cl.count(1)
    if count_1 == 0:
        print(f'#{t} -1')
        continue

    min_days = float('inf')

    for start in range(7):
        days = 0
        cnt = 0
        idx = start

        while cnt < n:
            if cl[idx % 7] == 1:
                cnt += 1
            days += 1
            idx += 1

        min_days = min(min_days, days)

    print(f'#{t} {min_days}')