T = int(input())
for t in range(1, T + 1):
    s = list(input())
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])
        else:
            if stack[-1] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])
    print(f'#{t} {len(stack)}')



