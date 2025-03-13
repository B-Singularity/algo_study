def recur(cnt, current, M, N, cache):
    result = []

    if cnt == M:
        return [current.copy()]
    for i in range(1, N + 1):
        if i in cache:
            continue
        current.append(i)
        cache.add(i)
        result.extend(recur(cnt + 1, current, M, N, cache))
        current.pop()
        cache.remove(i)
    return result


N, M = map(int, input().split())
result = recur(0, [], M, N, set())
for pair in result:
    print(' '.join(map(str, pair)))
