def is_palindrome(s, l, r, cnt):
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    else:
        return is_palindrome(s, l + 1, r - 1, cnt + 1)

T = int(input())
for t in range(1, T + 1):
    s = input()
    v, cnt = is_palindrome(s, 0, len(s) - 1, 1)
    print(v, cnt)