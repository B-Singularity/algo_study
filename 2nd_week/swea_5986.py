
def get_prime_list(n):
    """에라토스테네스의 체를 사용해 n 이하의 소수를 구하는 함수"""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(n ** 0.5) + 1):  # 괄호 위치 수정
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    return [num for num, prime in enumerate(is_prime) if prime]  # 소수 리스트 반환


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    prime_list = get_prime_list(N)
    size = len(prime_list)
    cnt = 0

    for i in range(size):
        left, right = i, size - 1
        while left <= right:
            total = prime_list[i] + prime_list[left] + prime_list[right]
            if total == N:
                cnt += 1
                left += 1
                right -= 1
            elif total < N:
                left += 1
            else:
                right -= 1

    print(f'#{t} {cnt}')