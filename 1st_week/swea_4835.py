T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    window = sum(arr[:M])
    max_value = window
    min_value = window

    for i in range(N - M):
        max_value = max(max_value, window)
        min_value = min(min_value, window)
        window = window - arr[i] + arr[i + M]
        print(f'{window} {arr[i]} {arr[i + M]} {min_value} {max_value}')
    max_value = max(max_value, window)
    min_value = min(min_value, window)
    print(f'#{t} {max_value - min_value}')
