T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    check = [arr[i] == i + 1 for i in range(N)]

    cnt = 0
    for i in range(N - 1, -1, -1):
        if not check[i]:
            cnt += 1
            for j in range(i + 1):
                check[j] = not check[j]

    print(f'#{t} {cnt}')