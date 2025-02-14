def find_kth_char(n, k):
    if n == 0:  # P0 = "0"
        return '0'
    if n == 1:  # P1 = "001"
        return "001"[k - 1]

    prev_length = (1 << (n - 1)) - 1  # P_(n-1)의 길이 = 2^(n-1) - 1

    if k <= prev_length:
        return find_kth_char(n - 1, k)  # 좌측 부분 (P_(n-1))
    elif k == prev_length + 1:
        return '0'  # 중간 문자
    else:
        mirrored_k = 2 * prev_length + 2 - k  # 우측 부분에 대해 k 값을 변환
        return '1' if find_kth_char(n - 1, mirrored_k) == '0' else '0'  # f(g(P_(n-1))) 적용

T = int(input())
for t in range(1, T + 1):
    K = int(input())

    n = 1
    while (1 << n) - 1 < K:  # 2^n - 1 >= K가 될 때까지 n 증가
        n += 1

    result = find_kth_char(n, K)
    print(f'#{t} {result}')