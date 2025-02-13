T = int(input())
for t in range(1, T + 1):
    s = list(input())
    dic = {}
    arr = []
    for ch in s:
        dic[ch] = dic.get(ch, 0) + 1
    for k, v in dic.items():
        if v % 2 == 1:
            arr.append(k)
    arr.sort()

    if not arr:
        print(f'#{t} Good')
    else:
        print(f'#{t} {"".join(arr)}')