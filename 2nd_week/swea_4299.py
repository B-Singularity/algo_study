T = int(input())

for t in range(1, T + 1):
    D, H, M = map(int, input().split())

    if (D, H, M) < (11, 11, 11):
        print(f'#{t} -1')
    else:
        minutes = (D - 11) * 24 * 60 + (H - 11) * 60 + (M - 11)
        print(f'#{t} {minutes}')