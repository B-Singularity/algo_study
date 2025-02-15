T = int(input())
triples = [i ** 3 for i in range(1, 10 ** 6 + 1)]
for t in range(1, T + 1):
    N = int(input())
    left = 0
    right = 10 ** 6
    result = -2
    while left <= right:
        mid = (left + right) // 2
        cube = mid ** 3

        if triples[mid] == N:
            result = mid
            break
        elif triples[mid] < N:
            left = mid + 1
        else:
            right = mid - 1

    print(f'#{t} {result + 1}')

