T = int(input())
for t in range(1, T + 1):
    N, number = input().split()
    N = int(N)
    result = bin(int(number, 16))[2:]
    result = result.zfill(N*4)
    print(f'#{t} {result}')