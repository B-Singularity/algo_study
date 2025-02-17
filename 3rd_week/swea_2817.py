def dfs(arr, K, idx = 0, total = 0):
    if total == K:
        return 1
    if idx >= len(arr) or total > K:
        return 0

    return dfs(arr, K, idx + 1, total + arr[idx]) + dfs(arr, K, idx + 1, total)



T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [x for x in A if x <= K]
    print(f'#{t} {dfs(A, K, 0, 0)}')