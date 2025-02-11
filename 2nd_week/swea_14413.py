def check(arr, n, m):
    flag = True
    question = True
    point = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '#':
                flag = True
                question = False
                point = (i + j) % 2
                break
            if arr[i][j] == '.':
                flag = False
                point = (i + j) % 2
                question = False
    if question:
        return True
    else:
        if flag:
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == '?':
                        continue
                    if (i + j) % 2 == point:
                        if arr[i][j] != '#':
                            return False
                    else:
                        if arr[i][j] != '.':
                            return False

        if not flag:
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == '?':
                        continue
                    if (i + j) % 2 == point:
                        if arr[i][j] != '.':
                            return False
                    else:
                        if arr[i][j] != '#':
                            return False
        return True

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, (input().split()))
    A = [list(input()) for _ in range(N)]
    if check(A, N, M):
        print(f'#{t} possible')
    else:
        print(f'#{t} impossible')


