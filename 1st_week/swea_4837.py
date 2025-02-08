T = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for t in range(1, T + 1):
    cnt = 0
    total = 0
    N, K = map(int,input().split())

    for i in range(1 << 12):
        subset = []
        for j in range(12):
            if i & (1 << j):
                subset.append(arr[j])

        if sum(subset) == K and len(subset) == N:
            cnt += 1
    print(f'#{t} {cnt}')