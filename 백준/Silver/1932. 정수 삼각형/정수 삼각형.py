import sys

input = sys.stdin.readline

n = int(input())
graph = [[-1 for _ in range(501)] for _ in range(501)]
dp = [[-1 for _ in range(501)] for _ in range(501)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(len(data)):
        graph[i][j] = data[j]

answer = 0

dp[0][0] = graph[0][0]

for i in range(1, n):
    for j in range(i + 1):
        dp[i][j] = max(dp[i - 1][j] + graph[i][j], dp[i - 1][j - 1] + graph[i][j])

print(max(dp[n - 1]))