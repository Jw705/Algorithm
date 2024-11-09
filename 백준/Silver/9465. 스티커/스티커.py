import sys

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = []
    graph.append(list(map(int, input().split())))
    graph.append(list(map(int, input().split())))
    dp = [[0 for _ in range(n)] for _ in range(3)]
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]
    dp[2][0] = 0
    answer = 0
    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1], dp[2][i - 1]) + graph[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[2][i - 1]) + graph[1][i]
        dp[2][i] = max(dp[0][i - 1], dp[1][i - 1])
    print(max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1]))