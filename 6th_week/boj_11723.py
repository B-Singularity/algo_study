M = int(input())
opers = [input().split() for _ in range(M)]

S = 0
for oper in opers:
    if oper[0] == 'add':
        S |= 1 << (int(oper[1]) - 1)
    elif oper[0] == 'remove':
        S 
