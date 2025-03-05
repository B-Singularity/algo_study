def postorder(index, N, tree):
    if index * 2 > N:
        return tree[index]

    left = postorder(index * 2, N, tree)
    right = 0
    if index * 2 + 1 <= N:
        right = postorder(index * 2 + 1, N, tree)

    tree[index] = left + right
    return tree[index]


T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        index, value = map(int, input().split())
        tree[index] = value

    postorder(1, N, tree)

    print(f'#{t} {tree[L]}')

