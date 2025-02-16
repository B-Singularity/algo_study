t = int(input())

for tc in range(1, t + 1):
    s = input()
    if s == s[::-1] or '*' in s:
        result = "Exist"
    else:
        result = "Not exist"
    print(f'#{tc} {result}')
