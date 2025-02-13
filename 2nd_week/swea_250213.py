for t in range(1, 11):
    length = int(input())
    s = input()
    stack = []
    flag = True
    for ch in s:
        if ch == '(' or ch == '[' or ch == '{' or ch == '<':
            stack.append(ch)
        elif ch == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = False
                break
        elif ch == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = False
                break
        elif ch == '}':
            if stack and stack[-1] == '{':
                stack.pop()
            else:
                flag = False
                break
        elif ch == '>':
            if stack and stack[-1] == '<':
                stack.pop()
            else:
                flag = False
                break
    if flag and not stack:
        print(f'#{t} 1')
    else:
        print(f'#{t} 0')