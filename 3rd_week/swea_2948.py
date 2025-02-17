T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    first = set(list(input().split()))
    second = set(list(input().split()))
    result = first & second
    print(f'#{t} {len(result)}')

