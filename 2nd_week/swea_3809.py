t = int(input())

for tc in range(1, t + 1) :
    n = int(input())
    value = ''
    while True :
        value += ''.join(map(str, input().split()))
        if len(value) == n :
            break

    result = 0
    cnt = 0
    while True :
        if str(cnt) not in value :
            result = cnt
            break
        cnt += 1

    print('#%d %d' % (tc, result))