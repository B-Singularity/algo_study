T = int(input())
for t in range(1, T + 1):
    N, D = map(int, input().split())
    result = N // (2 * D + 1)
    if N % (2 * D + 1) != 0:
        result += 1
    print(f'#{t} {result}')