from itertools import combinations

T = int(input())
for t in range(1, T + 1):
    nums = list(map(int, input().split()))
    comb = combinations(nums, 3)
    result = sorted(list(set(sum(com) for com in comb)))
    print(f'#{t} {result[-5]}')