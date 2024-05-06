import sys

input = sys.stdin.readline

n = int(input())
data = [0] + list(map(int, input().split()))

X = [[0, 0]]
dp = [0] * (len(data))

for i in range(1, len(data)):
    current = 0
    for j in range(0, i):
        if data[j] < data[i] and dp[j] > current:
            current = dp[j]
    dp[i] = current + 1

print(max(dp))