import sys

input = sys.stdin.readline

n, k = map(int, input().split())
prefix_sum = [0] * 1000001

for i in range(n):
    s, e = map(int, input().split())
    for j in range(s, e):
        prefix_sum[j] += 1

a = 0
b = 0
tmp_sum = 0
flag = False

while 0 <= a <= b and b < 1000001:
    if tmp_sum == k:
        flag = True
        break
    elif tmp_sum > k:
        tmp_sum -= prefix_sum[a]
        a += 1
    else:
        tmp_sum += prefix_sum[b]
        b += 1

if flag:
    print(a, b)
else:
    print(0, 0)

'''
4 25
0 10
3 15
0 8
3 10
'''
