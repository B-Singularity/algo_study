T = int(input())

for t in range(1, T + 1):
    flag = True
    N, M = map(int, input().split())

    # N 비트가 M의 마지막 N 비트에 모두 1인지 확인
    for i in range(N):
        if not (M & (1 << i)):  # M의 i번째 비트가 0인지 확인
            flag = False
            break

    if flag:
        print(f'#{t} ON')
    else:
        print(f'#{t} OFF')


