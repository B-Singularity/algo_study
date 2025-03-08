def cal_diff(arr, visited, N):
    start, link = 0, 0
    for i in range(N):
        for j in range(i + 1, N):
            if visited[i] and visited[j]:
                start += S[i][j] + S[j][i]
            elif not visited[i] and not visited[j]:
                link += S[i][j] + S[j][i]
    return abs(start - link)



def backtrack(idx, depth, visited, arr):
    if depth == N // 2:
        return cal_diff(arr, visited, len(arr))

    min_diff = float('inf')
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            diff = backtrack(i, depth + 1, visited, arr)
            min_diff = min(min_diff, diff)
            visited[i] = False
            if min_diff == 0:
                return 0
    return min_diff

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
result = backtrack(0, 0, visited, S)
print(result)
