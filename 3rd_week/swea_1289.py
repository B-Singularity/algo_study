T = int(input())
for t in range(1, T + 1):
    bit = list(input())
    cnt = 0
    i = 0
    while not all(bit) == '0' and i < len(bit):
        if bit[i] == '1':
            cnt += 1
            for j in range(i, len(bit)):
                if bit[j] == '1':
                    bit[j] = '0'
                else:
                    bit[j] = '1'
        i += 1
    print(f'#{t} {cnt}')



