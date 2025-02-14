from itertools import combinations

def check(n):
    n = str(n)
    for i in range(1, len(n)):
        if int(n[i]) < int(n[i - 1]):
            return False
    return True

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    comb = combinations(A, 2)
    max_value = -1
    for com in comb:
        if check(com[0] * com[1]):
            max_value = max(max_value, com[0] * com[1])

        print(f'#{t} {max_value}')

