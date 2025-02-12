T = int(input())
for t in range(1, T + 1):
    N = int(input())
    p = list(map(int, input().split()))
    min_idx = 0
    max_idx = 0

    cnt = 0
    for i in range(1, len(p) - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            cnt += 1
    print(f'#{t} {cnt}')