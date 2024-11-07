import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

prefix_sum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
prefix_sum[1][1] = graph[0][0]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix_sum[i][j] = graph[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(prefix_sum[x2][y2] - prefix_sum[x2][y1 - 1] - prefix_sum[x1 - 1][y2] + prefix_sum[x1 - 1][y1 - 1])
