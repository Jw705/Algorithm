def remove_110(string):
    stack = []
    count_110 = 0
    for char in string:
        stack.append(char)
        if len(stack) >= 3 and ''.join(stack[-3:]) == '110':
            stack.pop()
            stack.pop()
            stack.pop()
            count_110 += 1
    return ''.join(stack)


def solution(s):
    answer = []
    for string in s:
        str_remove_110 = remove_110(string)
        count_110 = (len(string) - len(str_remove_110)) // 3

        idx = str_remove_110.rfind('0')
        if idx == -1:
            # '0'이 없으면 문자열의 맨 앞에 삽입
            answer.append('110' * count_110 + str_remove_110)
        else:
            # '0'이 있으면 그 뒤에 110 삽입
            answer.append(str_remove_110[:idx + 1] + '110' * count_110 + str_remove_110[idx + 1:])

    return answer