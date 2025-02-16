def bubble(arr):
    for i in range(len(arr) - 1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble([1, 6, 2, 11, 3]))

def count(arr):
    count = [0] * (max(arr) + 1)
    result = [0] * len(arr)
    for num in arr:
        count[num] += 1
    for i in range(len(count) -1):
        count[i + 1] += count[i]

    for i in range(len(arr) - 1, -1, -1):
        count[arr[i]] -= 1
        result[count[arr[i]]] = arr[i]
    return result


print(count([1, 6, 2, 11, 3]))

def selection(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
print(selection([1, 6, 2, 11, 3]))