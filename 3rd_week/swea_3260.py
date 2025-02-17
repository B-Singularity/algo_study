T = int(input())
for t in range(1, T + 1):
    A, B = input().split()

    max_len = max(len(A), len(B))
    A = A.zfill(max_len)
    B = B.zfill(max_len)

    carry = 0
    result = []

    for i in range(max_len - 1, -1, -1):
        temp = int(A[i]) + int(B[i]) + carry
        if temp >= 10:
            carry = 1
            temp -= 10
        else:
            carry = 0
        result.append(str(temp))

    if carry:
        result.append("1")

    print(f'#{t} {"".join(result[::-1])}')




