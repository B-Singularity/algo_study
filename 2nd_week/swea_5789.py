T = int(input())
for t in range(1, T + 1):
    N, Q = map(int, input().split())
    changes = [list(map(int, input().split())) for _ in range(Q)]
    boxes = [0] * (N + 1)
    for i in range(len(changes)):
        L, R = changes[i]
        for j in range(L, R + 1):
            boxes[j] = i + 1
    print(f'#{t} {" ".join(map(str, boxes[1:]))}')


