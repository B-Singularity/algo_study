T = int(input())
for t in range(1, T + 1):
    p, q = map(float, input().split())
    if (1 - p) * q < p * (1 - q) * q:
        print(f'#{t} YES')
    else:
        print(f'#{t} NO')



    #p          1-p
    #q    1-q    0
    #s1 = p * q
    #s2 = ((1 - p) + p * (1 - q)) * q
