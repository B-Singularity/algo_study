def hanoi(n, start, end, other):
    if n == 1:
        return [(start, end)]
    else:
        moves = hanoi(n - 1, start, other, end)
        moves.append((start, end))
        moves.extend(hanoi(n - 1, other, end, start))
        return moves

N = int(input())

moves = hanoi(N, 1, 3, 2)
K = len(moves)

print(K)
for move in moves:
    print(move[0], move[1])

