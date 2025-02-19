from collections import deque

for t in range(1, 11):
    T = int(input())
    arr = deque(map(int, input().split()))
    i = 1
    while arr[-1] > 0:
        if i == 6:
            i = 1
        arr[0] = max(0, arr[0] - i)
        arr.rotate(-1)
        i += 1
    print(f'#{t} {" ".join(map(str, arr))}')

