TC = int(input())
for t in range(1, TC + 1):
    N, M = map(int, input().split())
    S = list(input().split())
    T = list(input().split())
    Q = int(input())
    cycle = len(S) * len(T)
    arr = [int(input()) % cycle for _ in range(Q)]
    result = []
    for num in arr:
        quo = num % len(S)
        rem = num % len(T)
        result.append(S[quo - 1] + T[rem - 1])
    st = ' '.join(result)
    print(f'#{t} {st}')
