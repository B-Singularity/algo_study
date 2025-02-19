from collections import deque

T = int(input().strip())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    C = list(map(int, input().split()))
    i = N
    cnt = 0
    pit = deque()
    for i in range(N):
        pit.appendleft([C[i], i])

    k = N
    result = -1

    cnt = 0
    while pit :
        if cnt == N:
            cnt = 0
            for ch in pit:
                ch[0] = ch[0] // 2

        if pit[0][0] == 0:
            result = pit.popleft()[1]
            if k < M:
                pit.appendleft([C[k], k])
                k += 1

        pit.rotate(-1)
        cnt += 1

    print(f'#{t} {result + 1}')



