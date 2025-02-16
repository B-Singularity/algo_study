T = int(input())

for t in range(1, T + 1):
    N = int(input())
    happy_days = [int(input()) for _ in range(N)]

    cnt = 0
    visited = [False] * N

    for i in range(1, N):
        if all(visited):
            break

        if not visited[i]:
            dis = happy_days[i] - happy_days[0]
            for j in range(i, N):
                if (happy_days[j] - happy_days[i]) % dis == 0:
                    visited[j] = True
            cnt += 1

    print(f'#{t} {cnt}')




