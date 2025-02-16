T = int(input())
for i in range(1, T + 1):
    total = 0
    scores = list(map(int, input().split()))
    for score in scores:
        if score < 40:
            total += 40
        else:
            total += score
    print(f'#{i} {total // len(scores)}')