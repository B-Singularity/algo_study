def check(st, word_to_find):
    cnt = 0
    flag = True
    if len(st) < len(word_to_find):
        return 0
    else:
        for i in range(len(st) - len(word_to_find) + 1):
            for j in range(len(word_to_find)):
                if st[i+j] != word_to_find[j]:
                    flag = False
                    break
            if flag:
                cnt += 1
            else:
                flag = True
        return cnt

for _ in range(10):
    t = int(input())
    word_to_find = input()
    st = input()
    result = check(st, word_to_find)
    print(f'#{t} {result}')
