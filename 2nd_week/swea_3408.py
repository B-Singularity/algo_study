T = int(input())
for t in range(1, T + 1):
    N = int(input())
    s1 = ((1 + N) * N) // 2
    s2 = ((2 * N) * N) // 2
    s3 = ((2 + 2 * N) * N) // 2
    print(f'#{t} {s1} {s2} {s3}')
