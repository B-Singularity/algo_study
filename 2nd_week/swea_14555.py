T = int(input())

for t in range(1, T + 1):
    S = input()
    length = len(S)
    S += ".."
    cnt = 0
    for i in range(length):
        if S[i] == '(' or S[i] == ')':
            cnt += 1
        if S[i] == '(' and S[i + 1] == ')':
            cnt -= 1

    print(f'#{t} {cnt}')

