def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        print(mid)
        if arr[mid] == key:
            return cnt
        elif arr[mid] < key:
            left = mid
        else:
            right = mid
        cnt += 1


T = int(input())
for t in range(1, T + 1):
    pages_to_find = list(map(int, input().split()))
    arr = [i for i in range(1, pages_to_find[0] + 1)]
    cnt1 = binary_search(arr, pages_to_find[1])
    cnt2 = binary_search(arr, pages_to_find[2])
    result = ""
    if cnt1 > cnt2:
        result = "B"
    if cnt1 < cnt2:
        result = "A"
    if cnt1 == cnt2:
        result = "0"
    print(f"#{t} {result}")