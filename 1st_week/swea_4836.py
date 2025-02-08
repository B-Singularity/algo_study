T = int(input())
for t in range(1, T + 1):
    cnt = 0
    N = int(input())
    check_red = [[False] * 10 for _ in range(10)]
    check_blue = [[False] * 10 for _ in range(10)]
    for i in range(N):
        y1, x1, y2, x2, color = map(int, input().split())
        if color == 1:
            for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    if not check_red[i][j]:
                        check_red[i][j] = True

        if color == 2:
            for i in range(y1, y2 + 1):
                for j in range(x1, x2 + 1):
                    if not check_blue[i][j]:
                        check_blue[i][j] = True

    for i in range(10):
        for j in range(10):
            if check_red[i][j] and check_blue[i][j]:
                cnt += 1


    print(f'#{t} {cnt}')