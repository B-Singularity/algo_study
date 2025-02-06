T = int(input())
for t in range(1, T + 1):
    K, N, M = map(int, input().split())
    station = list(map(int, input().split()))
    locate = [0] * (N + 1)
    locate.__next__()
    for num in station:
        locate[num] += 1
    energy = K
    cnt = 0
    now = 0
    flag = True
    while flag:
        if energy <= 0:
            cnt = 0
            break
        for i in range(now + K, now, -1):
            if now + energy >= N:
                flag = False
                break
            energy -= 1
            if i > N:
                flag = False
                break
            if locate[i] == 1:
                now = i
                energy = K
                cnt += 1
                break
    print(f'#{t} {cnt}')





