def contour(s):
    if len(s) == 1:
        return s
    third = len(s) // 3
    return contour(s[:third]) + " " * third + contour(s[2 * third:])

N = int(input())
line = '-' * (3 ** N)
print(contour(line))