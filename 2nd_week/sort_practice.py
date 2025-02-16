def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def counting_sort(arr):
    count = [0] * (max(arr) + 1)
    result = [0] * len(arr)

    for num in arr:
        count[num] += 1
    for i in range(len(count) - 1):
        count[i + 1] += count[i]
    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        result[count[arr[i]]] = arr[i]
    return result

def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

print(bubble_sort([1, 6, 2, 11, 3]))
print(counting_sort([1, 6, 2, 11, 3]))
print(selection_sort([1, 6, 2, 11, 3]))