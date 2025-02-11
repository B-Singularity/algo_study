def check(arr):
    ck = [False] * 8
    for i in range(8):
        if arr[i].count('O') != 1:
            return False
        for j in range(8):
            if arr[i][j] == 'O':
                if ck[j] == True:
                    return False
                else:
                    ck[j] = True

    return True



T = int(input())
for t in range(1, T + 1):
    chess = [list(input()) for _ in range(8)]
    if check(chess):
        print(f'#{t} yes')
    else:
        print(f'#{t} no')