def make_lcs_strings(x, y, z):
    ab = '0' * x
    bc = '1' * y
    ca = '0' * z

    A = ab + ca
    B = ab + bc
    C = bc + ca
    return A, B, C

T = int(input())
for t in range(1, T + 1):
    x, y, z = map(int, input().split())
    a, b, c = make_lcs_strings(x, y, z)
    print(f'# {t} {a} {b} {c}')

