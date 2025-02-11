T = int(input())

for t in range(1, T + 1):
    S = input()
    length = len(S)
    cnt = S.count('o')
    if 15 - length + cnt >= 8:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')