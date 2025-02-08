def is_pelindrom(s):
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True

TC = int(input())
for t in range(1, TC + 1):
    N, M = map(int, input().split())
    cnt = 0
    pelin_cnt = False
    arr = [input() for _ in range(N)]
    for st in arr:
        if st[::-1] in arr and not is_pelindrom(st):
            cnt += M
        if is_pelindrom(st) and not pelin_cnt:
            cnt += M
            pelin_cnt = True
    print(f'#{t} {cnt}')



