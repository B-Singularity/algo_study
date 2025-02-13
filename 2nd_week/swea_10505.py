T = int(input())
for t in range(1, T + 1):
    N = int(input())
    income = list(map(int, input().split()))
    mean = sum(income) / len(income)
    cnt = 0
    for money in income:
        if mean >= money:
            cnt += 1
    print(f'#{t} {cnt}')