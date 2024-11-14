T = int(input())

pibo = [0] * 101
pibo[1] = 1
pibo[2] = 1
for i in range(3, 101):
    pibo[i] = pibo[i - 1] + pibo[i - 2]

prefix_sum = [0] * 101
for i in range(1, 101):
    prefix_sum[i] = prefix_sum[i - 1] + pibo[i]

last = ''
ans = [''] * 101
for i in range(1, 101):
    if prefix_sum[i] % 2 == 1:
        ans[i] = 'impossible'
    else:
        answer = last
        sum_a = 0
        sum_b = 0
        for j in range(i - len(last), len(last)):
            if last[j] == 'A':
                sum_a += pibo[i - len(last) + j]
            else:
                sum_b += pibo[i - len(last) + j]

        if (i - len(last)) == 2:
            answer = 'BA' + answer
        elif sum_a <= sum_b:
            answer = 'A' + answer
        else:
            answer = 'B' + answer

        ans[i] = answer
        last = answer

for test_case in range(1, T + 1):
    n = int(input())
    print(ans[n])