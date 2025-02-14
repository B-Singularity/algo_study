def hanoi(n, start, end, via):
    if n == 1:
        return [(start, end)]
    else:
        moves = hanoi(n - 1, start, via, end)
        moves.append((start, end))
        moves.extend(hanoi(n - 1, via, end, start))


