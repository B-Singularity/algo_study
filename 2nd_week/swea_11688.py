T = int(input())
for t in range(1, T + 1):
    S = input()
    now = [1, 1]
    for ch in S:
        if ch == 'L':
            now[1] = now[0] + now[1]
        else:
            now[0] = now[0] + now[1]
    print(f'#{t} {" ".join(map(str, now))}')
