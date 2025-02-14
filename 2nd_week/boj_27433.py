def get_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * get_factorial(n - 1)


N = int(input())
print(get_factorial(N))