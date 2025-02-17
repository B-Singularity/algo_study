T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    result = (A ** 2) // (B ** 2)
    print(f'#{t} {result}')