def get_postfix(expression):
    operators = {'+':1}
    stack = []
    result = []

    for token in expression:
        if token.isalnum():
            result.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and operators[stack[-1]] >= operators[token]:
                result.append(stack.pop())
            stack.append(token)

    while stack:
        result.append(stack.pop())

    return result

def evaluate(expression):
    stack = []
    for token in expression:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
    return stack[0]

for t in range(1, 11):
    N = int(input())
    expression = input()
    print(f'#{t} {evaluate(get_postfix(expression))}')

