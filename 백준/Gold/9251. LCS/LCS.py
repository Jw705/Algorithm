import sys

input = sys.stdin.readline

str1 = input()
str2 = input()

n = max(len(str1)-1, len(str2)-1)
dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

answer = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i >= len(str2) or j >= len(str1):
            continue
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


print(answer)