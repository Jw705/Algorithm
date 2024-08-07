import sys

input = sys.stdin.readline

n, m = map(int, input().split())

data = [[]]
dp = [[0] * (n + 1) for _ in range(m + 1)]
dp2 = [[[0 for _ in range(m + 1)] for _ in range(n + 1)] for _ in range(m + 1)]

for _ in range(n):
    data.append(list(map(int, input().split())))

# print(data)
# print(dp)

for i in range(1, m + 1):
    for j in range(1, n + 1):
        # print('i=', i, 'j=', j)
        for k in range(1, j + 1):
            # dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i - 1][j - k] + data[k][i])

            # dp[i][j] = max(dp[i][j], dp[i - 1][j - k] + data[k][i])
            if dp[i][j] < dp[i - 1][j - k] + data[k][i]:
                dp[i][j] = dp[i - 1][j - k] + data[k][i]
                dp2[i][j] = dp2[i - 1][j - k].copy()
                dp2[i][j][i] += k

        if dp[i][j] < dp[i - 1][j]:
            dp[i][j] = dp[i - 1][j]
            dp2[i][j] = dp2[i - 1][j].copy()
        # print(dp)


print(dp[m][n])
for i in range(1, m + 1):
    print(dp2[m][n][i], end=' ')