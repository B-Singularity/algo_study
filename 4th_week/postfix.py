def postfix(expression):
    operations = {'+':1, '-':1, '*':2, '/':2, '^':3}
    stack = []
    output = []

    for token in expression:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and operations.get(stack[-1], 0) >= operations.get(token, 0):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def evaluate_postfix(expression):
    stack = []

    for token in expression:
        if token.isdigit():
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)

    return stack[0]
