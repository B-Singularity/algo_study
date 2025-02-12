def check(n):
    for i in range(1, 10):
        if n % i == 0:
            if 1 <= n // i <= 9:
                return 'Yes'
    return 'No'


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print(f'#{t} {check(N)}')
