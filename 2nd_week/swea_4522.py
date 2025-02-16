T = int(input())
for t in range(1, T + 1):
    s = input()
    result = 'Exist'
    for i in range(len(s)):
        if s[i] == s[len(s) - 1 - i] or s[i] == '?' or s[len(s) - 1 - i] == '?':
            continue
        else:
            result = 'Not exist'
            break
    print(f'#{t} {result}')
