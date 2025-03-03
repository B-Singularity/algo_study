def backtrack(current):
    if len(current) == N:
        print(" ".join(map(str, current)))
        return
    for num in range(1, N + 1):
        if num not in current:
            current.append(num)
            backtrack(current)
            current.pop()

N, M = map(int, input().split())
backtrack([])