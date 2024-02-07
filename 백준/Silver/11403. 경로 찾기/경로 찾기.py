INF = int(1e9)

n = int(input())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n) for _ in range(n)]

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 0:
            graph[i][j] = INF
        else:
            graph[i][j] = data[j]

# 점화식에 따라 플로이드 워셜 알고리즘을 수햄
for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()

'''
3
0 1 0
0 0 1
1 0 0
'''
