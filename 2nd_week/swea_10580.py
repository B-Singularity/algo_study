T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cnt = 0
    pole = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if pole[i][0] < pole[j][0] and pole[j][1] < pole[i][1]:
                cnt += 1
            elif pole[j][0] < pole[i][0] and pole[i][1] < pole[j][1]:
                cnt += 1
    print(f'#{t} {cnt}')
