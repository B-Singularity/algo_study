T = int(input())
def swap(i, j, string):
    s_list = list(string)
    s_list[i], s_list[j] = s_list[j], s_list[i]
    number = ''.join(s_list)
    return number
for test_case in range(1, T + 1):
    num = input().rstrip()
    result_min = int(num)
    result_max = int(num)
    for i in range(len(num)-1):
        for j in range(i, len(num)):
            number = swap(i, j, num)
            if number[0] == '0':
                continue
            if int(number) > result_max:
                result_max = int(number)
            if int(number) < result_min:
                result_min = int(number)
    print(f'#{test_case} {result_min} {result_max}')
