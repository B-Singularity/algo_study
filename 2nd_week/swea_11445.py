T = int(input())

for t in range(T):
    p = input().strip()
    q = input().strip()
    flag = 'Y'

    if p + 'a' == q:
        flag = 'N'

    print(f'#{t + 1}', flag)
