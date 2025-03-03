
def backtrack(current, N, M):
    result = []
    if len(current) == M:
        return [current.copy()]

    for i in range(1, N + 1):
        current.append(i)
        result.extend(backtrack(current, N, M))
        current.pop()
    return result

N, M = map(int, input().split())
result = sorted(backtrack([], N, M))
for item in result:
    print(" ".join(map(str, item)))
