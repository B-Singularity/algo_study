T = int(input())
for t in range(1, T + 1):
    str1 = input()
    str2 = input()
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    result = 0
    for i in range(len(str2) - len(str1) + 1):
        if str1 == str2[i:i + len(str1)]:
            result = 1
    print(f'#{t} {result}')