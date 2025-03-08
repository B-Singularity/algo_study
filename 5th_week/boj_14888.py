def dfs(idx, current, numbers, operators):
    if idx == len(numbers):
        return current, current

    min_value = float('inf')
    max_value = float('-inf')
    next_num = numbers[idx]

    for operator in operators:
        if operators[operator] > 0:
            operators[operator] -= 1

            if operator == '+':
                new_value = current + next_num
            elif operator == '-':
                new_value = current - next_num
            elif operator == '*':
                new_value = current * next_num
            elif operator == '/':
                if current < 0:
                    new_value = -(-current // next_num)
                else:
                    new_value = current // next_num

            sub_min, sub_max = dfs(idx + 1, new_value, numbers, operators)
            min_value = min(min_value, sub_min)
            max_value = max(max_value, sub_max)
            operators[operator] += 1

    return min_value, max_value

N = int(input())
A = list(map(int, input().split()))
operations_count = list(map(int, input().split()))
operators = {'+': operations_count[0], '-': operations_count[1],
             '*': operations_count[2], '/': operations_count[3]}

min_value, max_value = dfs(1, A[0], A, operators)

print(max_value)
print(min_value)
