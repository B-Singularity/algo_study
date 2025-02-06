T = int(input())
for t in range(1, T + 1):
    N = int(input())
    number = input()
    arr = [0] * 10
    cnt = -1
    max_num = -1
    for i in range(len(number)):
        num = int(number[i])
        arr[num] += 1

    for i in range(10):
        if cnt <= arr[i]:
            cnt = arr[i]
            max_num = i
    print(f'#{t} {max_num} {cnt}')


