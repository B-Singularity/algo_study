T = int(input())
for t in range(1, T + 1):
    N = int(input())
    a = list(map(int, input().split()))
    a.append('X')
    result = []
    cnt = 0
    empty_loc = N + 1
    for i in range(1, N + 1):
        if a[i - 1] != i:
            a[empty_loc - 1], a[i - 1] = a[i - 1], a[empty_loc - 1]
            empty_loc = i
            result.append(empty_loc)
            break
    for _ in range(1499):
        if empty_loc == N + 1:
            break
        target_index = a.index(empty_loc)  # 현재 empty_loc에 맞는 상자가 있는 칸 (0-indexed)
        move = target_index + 1  # 옮길 상자가 있는 칸 번호
        result.append(move)  # move를 결과에 기록
        a[empty_loc - 1], a[target_index] = a[target_index], a[empty_loc - 1]  # 상자 이동(스왑)
        empty_loc = move

    if not result:
        print(f'#{t} 0\n')
    else:
        print(len(result))
        print(f'#{t} {" ".join(map(str, result))}\n')
    # 2 3 4 1 X
    # X 3 4 1 2
    # 1 3 4 X 2
    # 1 3 X 4 2
    # 1 X 3 4 2
    # 1 2 3 4 X
    # 2 1 4 3 2

