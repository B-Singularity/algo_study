T = int(input())
for t in range(1, T + 1):
    S = input()
    cnt = 0
    i = 0
    j = len(S) - 1
    flag = True

    while i < j:
        if S[i] == S[j]:
            i += 1
            j -= 1
        elif S[i] == 'x':
            i += 1
            cnt += 1
        elif S[j] == 'x':
            j -= 1
            cnt += 1
        else:
            flag = False
            break

    if flag:
        print(f'{cnt}')
    else:
        print(f'-1')

