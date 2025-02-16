T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    scores.sort(reverse=True)
    print(f'#{t} {sum(scores[:K])}')
