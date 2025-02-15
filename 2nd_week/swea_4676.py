T = int(input())

for t in range(1, T + 1):
    s = list(input())
    H = int(input())
    hai = list(map(int, input().split()))

    hai.sort(reverse=True)

    for h in hai:
        s.insert(h, '-')

    print(f'#{t} {"".join(s)}')