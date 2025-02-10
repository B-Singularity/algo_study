def selection_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        min_idx = i
        for j in range(i, N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr

arr = [10, 25, 64, 22, 11]

print(selection_sort(arr))