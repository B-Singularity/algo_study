T = int(input())
for t in range(1, T + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]

    result = 0

    for i in range(N):
        if i <= N // 2:
            start = N // 2 - i
            end = N // 2 + i
        else:
            start = i - N // 2
            end = N - (i - N // 2) - 1

        result += sum(farm[i][start:end + 1])

    print(f'#{t} {result}')
