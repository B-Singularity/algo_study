T = int(input())
for t in range(1, T + 1):
    A, B, C, D = map(int, input().split())
    if B <= C or D <= A:
        result = 0
    # A C B D
    elif A <= C and B <= D:
        result = B - C
    # A C D B
    elif A <= C and D <= B:
        result = D - C
    # C A D B
    elif C <= A and D <= B:
        result = D - A
    # C A B D
    elif C <= A and B <= D:
        result = B - A
    print(f'#{t} {result}')
