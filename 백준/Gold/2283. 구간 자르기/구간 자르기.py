import sys

input = sys.stdin.readline

n, k = map(int, input().split())
prefix_sum = [0] * 1000001

for i in range(n):
    s, e = map(int, input().split())
    prefix_sum[s] += 1
    prefix_sum[e] -= 1

current = 0
for i in range(0, 1000001):
    current += prefix_sum[i]
    prefix_sum[i] = current

a = 0
b = 1
tmp_sum = prefix_sum[0]

while a <= b and b < 1000001:
    if tmp_sum == k:
        print(a, b)
        sys.exit()
    elif tmp_sum > k:
        tmp_sum -= prefix_sum[a]
        a += 1
    else:
        tmp_sum += prefix_sum[b]
        b += 1

print(0, 0)