T = int(input())
for t in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = [i for i in range(1, N + 1)]
    arr = list(map(int, input().split()))
    for num in arr:
        num_list.remove(num)
    num_list.sort()
    print(f'#{t} {" ".join(list(map(str, num_list)))}')
