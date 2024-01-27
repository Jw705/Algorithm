import sys

sys.setrecursionlimit(10 ** 6)

n, m, a, b, c = map(int, input().split())

# 그래프(트리)를 인접리스트 형태로 저장할 이차원 리스트 초기화
graph = [[] for _ in range(n + 1)]
# 노드의 방문 여부를 저장할 리스트 초기화
visited = [False] * (n + 1)

# 입력을 받아 트리 생성
for i in range(0, m):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[0]].append([data[1], data[2]])
    graph[data[1]].append([data[0], data[2]])

result = -1


def dfs(v, money, max_charge):
    global result
    if v == b:
        # print([v, money, max_charge], end=' ')
        result = max(result, max_charge)

    else:
        visited[v] = True
        # print(v, end=' ')
        for i in graph[v]:
            if (not visited[i[0]]) and money - i[1] >= 0:
                dfs(i[0], money - i[1], max(max_charge, i[1]))


dfs(a, c, 0)
print(result)

'''
5 5 1 3 10
1 2 5
2 3 5
1 4 1
4 5 6
5 3 1
'''
