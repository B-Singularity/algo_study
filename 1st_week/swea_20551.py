def check(box1, box2, box3):
    cnt = 0
    if box3 <= box2:
        cnt += box2 - box3 + 1
        box2 = box3 - 1
    if box2 == 0:
        return -1
    if box2 <= box1:
        cnt += box1 - box2 + 1
        box1 = box2 - 1
    if box1 == 0:
        return -1
    return cnt


T = int(input())
for t in range(1, T + 1):
    box1, box2, box3 = map(int, input().split())
    cnt = 0
    print(f'#{t} {check(box1, box2, box3)}')
