T = int(input())
result = []
for t in range(1, T + 1):

    n = list(input())
    while len(n) > 1:
        n = list(str(sum(map(int, n))))
    n = "".join(n)
    result.append(f'#{t} {n}')
print('\n'.join(result))