T = int(input())
for _ in range(1, T + 1):
    input_st = input().split()
    t = input_st[0]
    N = int(input_st[1])
    st = list(input().split())
    result = [0] * len(st)

    st_to_number = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    count = [0] * 10
    for ch in st:
        count[st_to_number[ch]] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]

    for j in range(len(st) - 1, -1, -1):
        num = st_to_number[st[j]]
        result[count[num] - 1] = st[j]
        count[num] -= 1

    print(f'{t}\n{" ".join(result)}')




