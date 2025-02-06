def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quick_sort(arr):
    stack = [(0, len(arr) - 1)]

    while stack:
        left, right = stack.pop()
        if left >= right:
            continue

        pivot = partition(arr, left, right)

        stack.append((left, pivot - 1))
        stack.append((pivot + 1, right))

    return arr

