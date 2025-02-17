from queue import PriorityQueue

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    actions = [list(map(int, input().split())) for _ in range(N)]
    que = PriorityQueue()
    result = []
    for action in actions:
        if len(action) == 2:
            que.put(-action[1])
        else:
            if not que.empty():
                result.append(-que.get())
            else:
                result.append("-1")

    print(f'#{t} {" ".join(map(str, result))}')