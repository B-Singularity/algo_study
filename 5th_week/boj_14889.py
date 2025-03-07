def backtrack(idx, depth, visited):
    if depth == N // 2:
        return cal_diff(visited)

    min_diff = float('inf')
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            diff =





N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
