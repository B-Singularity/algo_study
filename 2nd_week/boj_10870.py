def get_sol(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    return get_sol(n - 1) + get_sol(n - 2)

N = int(input())

print(get_sol(N))