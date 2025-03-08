def w(a, b, c, cache = None):
    if cache is None:
        cache = {}
    if (a, b, c) in cache:
        return cache[(a, b, c)]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        cache[(a, b, c)] = w(20, 20, 20, cache)
        return cache[(a, b, c)]
    if a < b and b < c:
        cache[(a, b, c)] = (
                w(a, b, c - 1, cache) +
                w(a, b - 1, c - 1, cache) -
                w(a, b - 1, c, cache)
        )
    else:
        cache[(a, b, c)] = (
            w(a - 1, b, c, cache) +
            w(a - 1, b - 1, c, cache) +
            w(a - 1, b, c - 1, cache) -
            w(a - 1, b - 1, c - 1, cache)
        )
    return cache[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if (a, b, c) == (-1, -1, -1):
        break
    result = w(a, b, c)
    print(f'w({a}, {b}, {c}) = {result}')

