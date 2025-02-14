T = int(input())
for t in range(1, T + 1):
    N = int(input())
    mean = [num[0] * num[1] for num in [list(map(float, input().split())) for _ in range(N)]]
    print(f'#{t} {sum(mean)}')