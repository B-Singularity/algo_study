T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, list(input())))
    cnt = arr[0]
    result = 0
    for i in range(1, len(arr)):
        if cnt >= i:
            cnt += arr[i]
        else:
            result += i - cnt
            cnt += i - cnt + arr[i]

    print(f'#{t} {result}')


