T = 10
for t in range(1, T + 1):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = 0
    for i in range(2, N - 2):
        now = buildings[i]
        max_value = max(max(buildings[i - 2:i]), max(buildings[i + 1:i + 3]))
        if now - max_value < 0:
            continue
        result += now - max_value
    print(f'#{t} {result}')
