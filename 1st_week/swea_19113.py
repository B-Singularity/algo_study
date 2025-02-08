TC = int(input())
for t in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    dic = {}
    result = []
    for i in range(2 * N):
        dic[arr[i]] = dic.get(arr[i], 0) + 1
    for i in range(2 * N):
        for j in range(i + 1, 2 * N):
            if arr[i] * (4 / 3) < arr[j]:
                break
            if arr[i] * (4 / 3) == arr[j] and dic[arr[j]] > 0 and dic[arr[i]] > 0:
                result.append(arr[i])
                dic[arr[i]] -= 1
                dic[arr[j]] -= 1
    result.sort()
    print(f'#{t} {" ".join(map(str, result))}')

