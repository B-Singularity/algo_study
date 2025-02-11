T = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for t in range(1, T + 1):
    now = 0
    st = input()
    cnt = 0
    for ch in st:

        if now != alphabet.index(ch):
            break
        else:
            now = alphabet.index(ch) + 1
            cnt += 1

    print(f'#{t} {cnt}')