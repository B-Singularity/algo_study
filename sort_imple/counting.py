def counting_sort(arr):
    if not arr:  # 빈 배열 예외 처리
        return []

    min_value = min(arr)
    max_value = max(arr)

    range_of_numbers = max_value - min_value + 1
    count = [0] * range_of_numbers
    result = [0] * len(arr)

    # 1️⃣ 카운트 배열 채우기
    for num in arr:
        count[num - min_value] += 1

        # 2️⃣ 누적 합 배열 만들기
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 3️⃣ 정렬 결과 채우기 (뒤에서부터 순회)
    i = len(arr) - 1
    while i >= 0:
        result[count[arr[i] - min_value] - 1] = arr[i]
        count[arr[i] - min_value] -= 1
        i -= 1

    return result


# 테스트
data = [0, -2, 4, 1, 11, -3, 6, 7]
print(counting_sort(data))  # [-3, -2, 0, 1, 4, 6, 7, 11]
