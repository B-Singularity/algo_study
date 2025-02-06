import sys
input = sys.stdin.readline

def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

N = int(input())
arr = [int(input()) for _ in range(N)]
answer = bubble_sort(arr)
for num in answer:
    print(num)