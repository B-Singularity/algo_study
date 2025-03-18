N, S = map(int, input().split())
length = 100001
arr = list(map(int, input().split()))
start = 0
end = 0
total = 0

while True:
    if total >= S:
        length = min(length, end - start)
        total -= arr[start]
        start += 1
    else:
        if end == N:
            break
        total += arr[end]
        end += 1

if length == 100001:
    print(0)
else:
    print(length)


