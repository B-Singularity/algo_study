import copy

def get_empty_cor(arr):
    location = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                location.append([i, j])
    return location

def check(arr, y, x):
    number = set(1, 2, 3, 4, 5, 6, 7, 8, 9)
    cnt_x = set()
    cnt_y = set()
    cnt_box = set()
    for i in range(9):
        cnt_x.add(arr[y][i])
    for i in range(9):
        cnt_y.add(arr[i][x])
    for i in range(3):
        for j in range(3):
            cnt_box.add(arr[y / 3 + i][x / 3 + j])
    if cnt_x != number or cnt_y != number or cnt_box != number:
        return False
    return True

def backtrack(arr, empty_loc, ):
    lst = copy.deepcopy(arr)
    for i in range(len(empty_loc)):
        y, x = empty_loc[i]
        for j in range(9):
            if check(lst, y, x):
                



sdoku = [list(map(int, input().split())) for _ in range(9)]

