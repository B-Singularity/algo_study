T = int(input())
for t in range(1, T + 1):
    s = input()
    vo = ['a', 'e', 'i', 'o', 'u']
    result = ''
    for ch in s:
        if ch not in vo:
            result += ch
    print(f'#{t} {result}')
