for t in range(1, 11):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    dx = [-1, 1, 0]
    dy = [0, 0, -1]
    x = -1
    for i in range(100):
        if arr[99][i] == 2:
            x = i
            break

    y = 99
    while y > 0:
        for j in range(3):
            new_x = x + dx[j]
            new_y = y + dy[j]
            if 0 <= new_x < 100 and 0 <= new_y < 100 and arr[new_y][new_x] == 1:
                arr[y][x] = -1
                x = new_x
                y = new_y
                break
    print(f'#{t} {x}')







