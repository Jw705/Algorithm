import sys
import math

input = sys.stdin.readline

n = int(input())

dp = [0] * 50001
제곱배열 = []

for i in range(1, n + 1):
    if math.sqrt(i) == int(math.sqrt(i)):
        dp[i] = 1
        제곱배열.append(i)
        maximum = i
    else:
        dp[i] = 1e9
        for j in 제곱배열:
            dp[i] = min(dp[i], dp[j] + dp[i - j])
        if dp[i] == 1e9:
            dp[i] = 0

print(dp[n])