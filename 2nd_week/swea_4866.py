T = int(input())
for t in range(1, T + 1):
    s = input()
    stack = []
    flag = True
    for i in range(len(s)):
        if s[i] == '(' or s[i] == '{':
            stack.append(s[i])
        elif s[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif s[i] == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                flag = False
                break

    if flag and not stack:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')

