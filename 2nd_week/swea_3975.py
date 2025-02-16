t = int(input())

result = []
for tc in range(1, t + 1) :
    a, b, c, d = map(int, input().split())
    alice = a / b
    bob = c / d

    if alice == bob :
        result.append('DRAW')
    elif alice > bob :
        result.append('ALICE')
    else :
        result.append('BOB')

for idx, value in enumerate(result) :
    print('#%d %s' % (idx + 1, value))