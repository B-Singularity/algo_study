T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))
    end_node = max(edges)
    left = [0] * (end_node + 1)
    right = [0] * (end_node + 1)
    for i in range(0, len(edges), 2):
        parent = edges[i]
        child = edges[i + 1]
        if left[parent] != 0:
            right[parent] = child
        else:
            left[parent] = child
    stack = [N]
    cnt = 1
    while stack:
        p = stack.pop()
        if left[p] != 0:
            cnt += 1
            stack.append(left[p])
        if right[p] != 0:
            cnt += 1
            stack.append(right[p])
    print(f'#{t} {cnt}')
