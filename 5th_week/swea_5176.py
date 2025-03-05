def inorder(idx, N, res, num):
    if idx > N:
        return num

    num = inorder(idx * 2, N, res, num)
    res[idx] = num
    num += 1
    num = inorder(idx * 2 + 1, N, res, num)
    return num

T = int(input())
for t in range(1, T + 1):
    i = 0
    N = int(input())
    res = [0] * (N + 1)
    inorder(1, N, res, 1)
    print(f'#{t} {res[1]} {res[N // 2]}')


