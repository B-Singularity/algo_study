T = int(input())
for t in range(1, T + 1):
    N, p_d, p_g = map(int, input().split())
    flag = True
    if (p_g == 100 or p_g == 0) and p_g != p_d:
        flag = False
    else:
        flag = False
        for i in range(1, N + 1):
            if i * p_d % 100 == 0:
                flag = True
                break
    if flag:
        print(f'#{t} Possible')
    else:
        print(f'#{t} Broken')
