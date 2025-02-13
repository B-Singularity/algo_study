T = int(input())
for t in range(1, T + 1):
    N, A, B = map(int, input().split())
    print(f'#{t} {min(A, B)} {abs(N - A - B) if N < A + B else 0}')