def recur(arr, cnt, N, visited, max_value):
    current_value = int(''.join(map(str, arr)))

    if (current_value, cnt) in visited:
        return max_value
    visited.add((current_value, cnt))

    if cnt == N:
        return max(max_value, current_value)

    for i in range(len(arr) - 1):
        for j in range(i + 1, len(arr)):
            arr[i], arr[j] = arr[j], arr[i]
            max_value = recur(arr, cnt + 1, N, visited, max_value)
            arr[i], arr[j] = arr[j], arr[i]

    return max_value



T = int(input())
for t in range(1, T + 1):
    num, cnt = input().split()
    cnt = int(cnt)
    num_list = list(map(int, num))
    visited = set()

    result = recur(num_list, 0, cnt, visited, -1)



    print(f'#{t} {result}')

    # 32888
    # 88832
    # 82388 82838 82883
    # 1개    3개   2개
