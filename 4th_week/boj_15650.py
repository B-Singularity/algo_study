def backtrack(index, current):
    result = []
    if len(current) == M:
        return [current.copy()]
    for i in range(index, N + 1):
        current.append(i)
        result.extend(backtrack(i + 1, current))
        current.pop()

    return result



N, M = map(int, input().split())
result = sorted(backtrack(1, []))
for item in result:
    print(" ".join(map(str, item)))
