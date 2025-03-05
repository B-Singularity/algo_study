def in_order(index, num, N, res):
    if index > N:
        return num

    num = in_order(index * 2, num, N, res)
    res[index] = num
    num += 1
    num = in_order(index * 2 + 1, num, N, res)
    return num



for t in range(1, 11):
    N = int(input())
    res = [0] * (N + 1)
    word_order = [list(input().split()) for _ in range(N)]
    dic = {i + 1: word_order[i][1] for i in range(N)}
    result = []
    in_order(1, 1, N, res)
    for i in range(1, N + 1):
        result.append(dic[res.index(i)])
    print(f'#{t} {"".join(map(str, result))}')
