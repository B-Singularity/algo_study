T = int(input())
for _ in range(T):
    X, S = map(int, input().split())

    # 기본 조건: S가 X보다 작거나, (S-X)가 홀수이면 불가능
    if S < X or (S - X) % 2 != 0:
        print(-1)
        continue

    # S와 X가 같은 경우
    if S == X:
        if S == 0:
            # 빈 배열: 길이가 0
            print(0)
        else:
            # 길이 1 배열: [X]
            print(1)
            print(X)
        continue

    # 일반적인 경우: S > X 인 상황
    Y = (S - X) // 2

    # 두 수의 비트 AND가 0이면 길이 2 배열, 그렇지 않으면 길이 3 배열
    if (X & Y) == 0:
        print(2)
        print(X + Y, Y)
    else:
        print(3)
        print(X, Y, Y)
