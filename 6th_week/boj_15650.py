def recur(start, current, cnt, N, M):
    result = []
    if cnt == M:
        return [current.copy()]

    for i in range(start, N + 1):
        current.append(i)
        result.extend(recur(i + 1, current, cnt + 1, N, M))
        current.pop()
    return result

N, M = map(int, input().split())
result = recur(1, [], 0, N, M)
print(result)
