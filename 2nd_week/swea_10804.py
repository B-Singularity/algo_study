T = int(input())
for t in range(1, T + 1):
    s = input()
    arr = []
    for ch in s:
        if ch == 'b':
            arr.append('d')
        elif ch == 'd':
            arr.append('b')
        elif ch == 'p':
            arr.append('q')
        elif ch == 'q':
            arr.append('p')
    arr.reverse()
    print(f'#{t} {"".join(arr)}')
