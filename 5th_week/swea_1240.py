# import sys
# sys.stdin = open("C:/Users/SSAFY/Downloads/input (5).txt", "r")


def extract_cod(arr, dic):
    result = []

    for row in arr:
        if '1' in row:
            row = row.rstrip('0')
            if len(row) >= 56:
                row = row[-56:]

                for i in range(0, 56, 7):
                    code = row[i:i + 7]
                    if code in dic:
                        result.append(dic[code])

                break

    return result


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    cod = [input() for _ in range(N)]
    dic = {'0001101':0, '0011001':1, '0010011':2, '0111101':3, '0100011':4, '0110001':5, '0101111':6, '0111011':7, '0110111':8, '0001011':9}
    secret = extract_cod(cod, dic)

    result = 0
    for i in range(len(secret)):
        if i % 2 == 0:
           result += secret[i] * 3
        else:
            result += secret[i]

    if result % 10 == 0:
        print(f'#{t} {sum(secret)}')
    else:
        print(f'#{t} 0')