def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(input())
for i in range(1, T + 1):
    str1, str2 = input().split()
    lcm_val = lcm(len(str1), len(str2))
    str1 = str1 * (lcm_val // len(str1))
    str2 = str2 * (lcm_val // len(str2))
    if str1 == str2:
        print(f'#{i} yes')
    else:
        print(f'#{i} no')
