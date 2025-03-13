def recur(current, cnt, N, M):
    result = []
    if cnt == M:
        return [current.copy()]
    for i in range(1, N + 1):
        current.append(i)
        result.extend(recur(current, cnt + 1, N, M))
        current.pop()
    return result
N, M = map(int, input().split())
result = recur([], 0, N, M)
print(result)