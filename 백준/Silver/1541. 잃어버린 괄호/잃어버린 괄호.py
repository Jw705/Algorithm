data = input()

num_list = []
operator_list = []
tmp_str = ''

for char in data:
    if char == '-' or char == '+':
        num_list.append(int(tmp_str))
        operator_list.append(char)
        tmp_str = ''
    else:
        tmp_str += char

num_list.append(int(tmp_str))

result = num_list[0]
tmp = 0

for i in range(len(operator_list)):
    if operator_list[i] == '+':
        if tmp < 0:
            tmp -= num_list[i + 1]
        else:
            tmp += num_list[i + 1]
    elif operator_list[i] == '-':
        result += tmp
        tmp = 0
        tmp -= num_list[i + 1]

result += tmp
print(result)
