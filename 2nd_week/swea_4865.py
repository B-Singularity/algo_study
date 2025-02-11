T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    dic = {}
    result = -1
    for ch in str2:
        dic[ch] = dic.get(ch, 0) + 1
    for ch in str1:
        if dic[ch] > result:
            result = dic[ch]
    print(f'#{t} {result}')