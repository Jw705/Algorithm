def strToInt(str):
    res = 0
    for c in range(len(str)):
        res = res + sorted_dict[str[c]]['value'] * (10 ** (len(str) - c - 1))
    return res

N = int(input())
list = []
input_dict = {}

for i in range(N):
    str = input()
    list.append(str)
    for j in range(len(str)):
        if str[j] in input_dict:
            input_dict[str[j]]['primitive_value'] += 10**(len(str) - j - 1)
        else:
            input_dict[str[j]] = {'primitive_value': 10**(len(str) - j - 1)}

sorted_dict = dict(sorted(input_dict.items(), key=lambda x: (x[1]['primitive_value']), reverse=True))

num = 9
for i in sorted_dict:
    sorted_dict[i]['value'] = num
    num = num - 1

res = 0
for word in list:
    res += strToInt(word)

print(res)
