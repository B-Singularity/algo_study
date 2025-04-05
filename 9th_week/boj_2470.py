import sys
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = N - 1
min_diff = float('inf')
answer = (0, 0)

while left < right:
    total = liquid[left] + liquid[right]

    if abs(total) < min_diff:
        min_diff = abs(total)
        answer = (liquid[left], liquid[right])

    if total < 0:
        left += 1
    else:
        right -= 1

print(answer[0], answer[1])
