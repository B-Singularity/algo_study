def deco(word):
    matrix = [[''] for _ in range(5)]
    first = '..#.'
    second = '.#.#'
    fourth = '.#.#'
    fifth = '..#.'
    for i in range(len(word)):
        matrix[0] += first
        matrix[1] += second
        matrix[2] += f'#.{word[i]}.'
        matrix[3] += fourth
        matrix[4] += fifth
    matrix[0] += '.'
    matrix[1] += '.'
    matrix[2] += '#'
    matrix[3] += '.'
    matrix[4] += '.'
    print('\n'.join([''.join(i) for i in matrix]))

T = int(input())
for t in range(1, T + 1):
    word = input()
    deco(word)


