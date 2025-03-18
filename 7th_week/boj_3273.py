N = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()
start = 0
end = N - 1
while arr[end // 2] >= x:
    end //= 2

cnt = 0
while start < end:
    if arr[start] + arr[end] > x:
        end -= 1
    elif arr[start] + arr[end] < x:
        start += 1
    else:
        cnt += 1
        start += 1
        end -= 1
print(cnt)