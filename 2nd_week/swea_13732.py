python
복사
편집


def check(arr, start_x, start_y, end_x, end_y):
    # 사각형 크기 확인
    side_length = end_x - start_x + 1
    if side_length != (end_y - start_y + 1):  # 정사각형인지 확인
        return False

    # 내부가 모두 '#'인지 확인
    for i in range(start_x, end_x + 1):
        for j in range(start_y, end_y + 1):
            if arr[i][j] == '.':
                return False
    return True


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    start_x, start_y = -1, -1
    end_x, end_y = -1, -1

    # '#'이 있는 최소 사각형 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '#':
                if start_x == -1:  # 처음 발견한 경우
                    start_x, start_y = i, j
                end_x, end_y = i, j  # 계속 갱신

    if check(arr, start_x, start_y, end_x, end_y):
        print(f'#{t} yes')
    else:
        print(f'#{t} no')

