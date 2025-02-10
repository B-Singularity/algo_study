def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    result = []
    for num in arr:
        count[num] += 1
    for i, num in enumerate(count):
        if num > 0:
            result.append(i)

    return result

data = [0, 2, 4, 1, 11, 3, 6, 7]
print(counting_sort(data))

