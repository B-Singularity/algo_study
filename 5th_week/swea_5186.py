T = int(input())
for t in range(1, T + 1):
    N = float(input())
    remain = N
    result = []
    i = -1
    while remain != 0:
        quo = remain // (2 ** i)
        result.append(quo)
        remain = remain % (2 ** i)
        i -= 1
    # print(result)
    if len(result) > 12:
        print(f'#{t} overflow')
    else:
        print(f'#{t} {"".join(map(str, map(int, result)))}')
