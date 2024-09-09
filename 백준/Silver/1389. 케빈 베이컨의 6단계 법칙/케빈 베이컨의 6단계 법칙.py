import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정

n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
min_cabin_bacon_num = INF

for a in range(1, n + 1):
    cabin_bacon_num = 0
    for b in range(1, n + 1):
        if a != b:
            cabin_bacon_num += graph[a][b]
    if cabin_bacon_num < min_cabin_bacon_num:
        min_cabin_bacon_num = cabin_bacon_num
        answer = a

print(answer)