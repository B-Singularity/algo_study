T = int(input())
for t in range(1, T + 1):
    N, M, K = map(int, input().split())
    waiting = list(map(int, input().split()))
    waiting.sort()

    time = 0
    fish = 0
    flag = True

    for i in range(N):
        while time < waiting[i]:
            time += 1
            if time % M == 0:
                fish += K

        if fish == 0:
            flag = False
            break

        fish -= 1

    if flag:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Impossible')