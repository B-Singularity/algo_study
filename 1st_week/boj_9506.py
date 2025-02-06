def get_divisor(n):
    result = []
    for i in range(1, int(n ** (1/2)) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
    return sorted(result)


while True:
    N = int(input())
    answer = f'{N} = '
    if N == -1:
        break
    divisor = get_divisor(N)
    if N == sum(divisor) - N:
        result = " + ".join(map(str, divisor[:-1]))
        print(f'{N} = {result}')
    else:
        print(f'{N} is NOT perfect.')