T = int(input())
for t in range(1, T + 1):
    A, B, C = map(int, input().split())
    if C < 3 or B < 2:
        print(f'#{t} -1')
    else:
        cnt = 0
        if B >= C:
            cnt += B - C + 1
            B = C - 1
            if A >= B:
                cnt += A - B + 1
        print(f'#{t} {cnt}')