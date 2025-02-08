T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    stuff = [list(map(int, input().split())) for _ in range(M)]
    box = [0] * (N + 1)
    for i in range(M):
        size, value = stuff[i]
        for j in range(N, size - 1, -1):
            box[j] = max(box[j], box[j - size] + value)

    print(f'#{t} {box[N]}')

