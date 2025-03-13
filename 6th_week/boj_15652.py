def recur(idx, current, cnt, N, M):
    result = []
    if cnt == M:
        return [current.copy()]
    for i in range(idx, N + 1):
        current.append(i)
        result.extend(recur(i, current, cnt + 1, N, M))
        current.pop()
    return result

N, M = map(int, input().split())
result = recur(1, [], 0, N, M)
print(result)