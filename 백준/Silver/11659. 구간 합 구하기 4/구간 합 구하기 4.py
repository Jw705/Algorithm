import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
prefix_sum[0] = 0
prefix_sum[1] = data[0]
for i in range(2, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + data[i - 1]

for _ in range(m):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i - 1])