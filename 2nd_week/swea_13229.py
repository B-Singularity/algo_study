T = int(input())
for t in range(1, T + 1):
    S = input()
    dic = {"MON":1, 'TUE':2, 'WED':3, 'THU':4, 'FRI':5, 'SAT':6, 'SUN':0}
    result = 7 - dic[S]
    print(f'#{t} {result}')
