

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    words = [input() for _ in range(N)]
    alphabet = [chr(ord('a') + i) for i in range(26)]
    cnt = 0
    for i in range(1, 1 << N):
        arr = []
        for j in range(N):
            if i & (1 << j):
                arr.extend(words[j])
        check = "".join(arr)
        flag = True
        for k in range(26):
            if alphabet[k] not in check:
                flag = False
                break
        if flag:
            cnt += 1
    print(f'#{t} {cnt}')


