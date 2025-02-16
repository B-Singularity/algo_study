T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    for i in range(3):
        if arr.count(arr[i]) == 1 or arr.count(arr[i]) == 3:
            print(f'#{t} {arr[i]}')
            break
