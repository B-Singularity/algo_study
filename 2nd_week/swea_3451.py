T = int(input())
for t in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X > U:
        print(f'#{t} -1')
    else:
        print(f'#{t} {max(0, (L - X))}')