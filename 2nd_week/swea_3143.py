def check(st, word_to_find):
    cnt = 0
    flag = True
    if len(st) < len(word_to_find):
        return st

    st = list(st)
    i = 0
    while i <= len(st) - len(word_to_find):
        if st[i:i+len(word_to_find)] == list(word_to_find):
            for j in range(i, i+len(word_to_find)):
                st[j] = '.'
            i += len(word_to_find)
        else:
            i += 1
    return len(st) - st.count('.') + st.count('.') // len(word_to_find)



T = int(input())
for t in range(1, T + 1):
    A, B = input().split()
    result = check(A, B)
    print(f'#{t} {result}')