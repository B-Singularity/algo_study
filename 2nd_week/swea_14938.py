T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = []
    arr.sort()
    i = 0
    j = N - 1
    while i <= j:
        result.append(arr[j])
        result.append(arr[i])
        i += 1
        j -= 1

    print(f'#{t} {" ".join(map(str, result[:10]))}')