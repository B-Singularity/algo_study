T = int(input())
for t in range(1, T + 1):
    word = [[-1] * 15 for _ in range(5)]
    for i in range(5):
        w = input()
        for j in range(len(w)):
            word[i][j] = w[j]

    answer = ""

    for i in range(15):
        for j in range(5):
            if word[j][i] != -1:
                answer += word[j][i]

    print(f'#{t} {answer}')