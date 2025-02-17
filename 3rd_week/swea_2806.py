def check(y, x, queens):
    for qy, qx in queens:
        if qx == x or abs(qy - y) == abs(qx - x):
            return False
    return True

def queen(y, N, queens):
    if y == N:
        return 1

    count = 0
    for x in range(N):
        if check(y, x, queens):
            count += queen(y + 1, N, queens + [(y, x)])

    return count


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    result = queen(0, N, [])
    print(f'#{t} {result}')
