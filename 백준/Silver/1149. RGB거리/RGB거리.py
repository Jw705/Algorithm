import sys

input = sys.stdin.readline

n = int(input())
arr = []

for i in range(n):
    r_cost, g_cost, b_cost = map(int, input().split())
    arr.append([r_cost, g_cost, b_cost])

dp = [[0, 0, 0] for _ in range(n)]

for i in range(n):
    if i == 0:
        dp[i] = arr[i]
    else:
        dp[i] = [min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0],
                 min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1],
                 min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]]

print(min(dp[n - 1]))