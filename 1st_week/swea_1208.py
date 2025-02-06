def find_idx(arr):
    min_height = 101
    min_idx = -1
    max_idx = -1
    max_height = -1
    for idx, box in enumerate(boxes):
        if box < min_height:
            min_height = box
            min_idx = idx
        if box > max_height:
            max_height = box
            max_idx = idx
    return min_height, min_idx, max_height, max_idx



for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    min_height = 101
    min_idx = -1
    max_idx = -2
    max_height = 0


    while dump > 0:
        min_height, min_idx, max_height, max_idx = find_idx(boxes)
        if min_idx == max_idx == 0 or max_height - min_height == 1:
            break
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        dump -= 1

    min_height, min_idx, max_height, max_idx = find_idx(boxes)
    print(f'#{t} {max_height - min_height}')






