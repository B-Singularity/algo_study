T = int(input())
for t in range(1, T + 1):
    A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    cnt = C // A
    cnt += (C - cnt * A) // B
    print(f'#{t} {cnt}')
