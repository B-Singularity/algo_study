T = int(input())
for t in range(1, T + 1):
    S = list(input())
    S_set = set(S)
    if len(S_set) == 2:
        min_cnt = 5
        for ch in S:
            if S.count(ch) < min_cnt:
                min_cnt = S.count(ch)
        if min_cnt == 2:
            print(f'#{t} Yes')
        else:
            print(f'#{t} No')
    else:
        print(f'#{t} No')

