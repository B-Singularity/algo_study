import sys

def merge_sort(arr):
    if len(arr) <= 1:  # 기저 사례: 배열의 크기가 1 이하일 경우
        return arr

    mid = len(arr) // 2  # 중간 인덱스 계산
    left_half = merge_sort(arr[:mid])  # 왼쪽 절반 정렬
    right_half = merge_sort(arr[mid:])  # 오른쪽 절반 정렬

    return merge(left_half, right_half)  # 병합 후 반환


def merge(left, right):
    sorted_arr = []
    i = j = 0

    # 두 리스트를 비교하며 정렬
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # 남은 원소 추가 (한쪽 배열이 먼저 끝났을 경우)
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(sys.stdin.readline().strip()))
answer = merge_sort(numbers)

for num in answer:
    print(num)