def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i - 1]:
            return False
    return True

T = int(input())
for t in range(1, T + 1):
    word = input().strip()

    flag = is_palindrome(word)

    if flag and not is_palindrome(word[:len(word) // 2]):
        flag = False

    if flag and not is_palindrome(word[len(word) // 2 + (len(word) % 2):]):
        flag = False

    print(f'#{t} {"YES" if flag else "NO"}')