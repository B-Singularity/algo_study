T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cards = list(input().split())
    result = []
    mid = (N + 1) // 2  # N이 홀수일 때 가운데 카드 포함

    for i in range(N // 2):
        result.append(cards[i])
        result.append(cards[mid + i])

    if N % 2 == 1:
        result.append(cards[N // 2])  # 가운데 카드 추가

    print(f'#{t} {" ".join(map(str, result))}')
