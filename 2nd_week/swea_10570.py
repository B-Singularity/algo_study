T = int(input())
for t in range(1, T + 1):
    A, B = map(int, input().split())
    arr = [1, 4, 9, 121, 484]
    cnt = 0
    for i in range(5):
        if A <= arr[i] <= B:
            cnt += 1
    print(f'#{t} {cnt}')
