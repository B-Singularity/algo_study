def check(arr):
    for count in arr:
        if count >= 3:
            return True

    for i in range(8):
        if arr[i] >= 1 and arr[i + 1] >= 1 and arr[i + 2] >= 1:
            return True
    return False




T = int(input())
for t in range(1, T + 1):
    arr = list(map(int, input().split()))
    player_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    player_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    result = 0
    for i in range(12):
        if i % 2 == 0:
            player_1[arr[i]] += 1
            if check(player_1):
                result = 1
                break
        if i % 2 != 0:
            player_2[arr[i]] += 1
            if check(player_2):
                result = 2
                break
    print(result)


    print(f'#{t} {result}')

