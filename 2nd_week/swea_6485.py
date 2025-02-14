T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    c = [int(input()) for _ in range(P)]
    result = []
    stop = [0] * 5001
    for i in range(len(arr)):
        a = arr[i][0]
        b = arr[i][1]
        for j in range(a, b + 1):
            stop[j] += 1
    for j in range(len(c)):
        result.append(stop[c[j]])
    print(f'#{t} {" ".join(map(str, result))}')

