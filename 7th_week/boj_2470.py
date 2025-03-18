N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N - 1
max_value = float('-inf')
answer1 = answer2 = 0

while start < end:
    total = arr[start] + arr[end]
    if (abs(max_value) > abs(total)):
        max_value = total
        answer1 = arr[start]
        answer2 = arr[end]

    if total < 0:
        start += 1
    else:
        end -= 1

print(answer1, answer2)