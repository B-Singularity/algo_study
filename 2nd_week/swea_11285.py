def get_score(a, b):
    radius = (a**2 + b**2) ** 0.5
    for i in range(1, 11):
        if radius <= i * 20:
            return 11 - i
    return 0

T = int(input())
result = []
for t in range(1, T + 1):
    N = int(input())
    score = 0
    for _ in range(N):
        a, b = map(int, input().split())
        score += get_score(a, b)

    result.append(f'#{t} {score}')

print("\n".join(result))


