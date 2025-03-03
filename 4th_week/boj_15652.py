def backtrack(start, current, N, M):
    result = []
    if len(current) == M:
        return [current.copy()]

    for i in range(start, N + 1):
        current.append(i)
        result.extend(backtrack(i, current, N, M))
        current.pop()
    return result

N, M =map(int, input().split())

result = backtrack(1,[], N, M)
for item in result:
    print(" ".join(map(str, item)))