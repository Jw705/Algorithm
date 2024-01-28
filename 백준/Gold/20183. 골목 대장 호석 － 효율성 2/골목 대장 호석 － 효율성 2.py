import sys

sys.setrecursionlimit(10 ** 6)

n, m, a, b, c = map(int, input().split())

# 그래프(트리)를 인접리스트 형태로 저장할 이차원 리스트 초기화
graph = [[] for _ in range(n + 1)]
# 노드의 방문 여부를 저장할 리스트 초기화
visited = [False] * (n + 1)
costs = []

# 입력을 받아 트리 생성
for i in range(0, m):
    data = list(map(int, sys.stdin.readline().split()))
    graph[data[0]].append([data[1], data[2]])
    graph[data[1]].append([data[0], data[2]])
    costs.append(data[2])

result = 10 ** 11
tmp = False


def dfs(v, money, max_charge):
    global tmp
    if v == b:
        # print([v, money, max_charge], end=' ')
        tmp = True
        return True

    else:
        visited[v] = True
        # print(v, end=' ')
        for i in graph[v]:
            if (not visited[i[0]]) and money - i[1] >= 0 and max_charge >= i[1]:
                dfs(i[0], money - i[1], max_charge)


'''
for i in range(len(costs)):
    tmp = False
    visited = [False] * (n + 1)
    dfs(a, c, costs[i])
    # print(costs[i], tmp)
    if tmp:
        result = min(result, costs[i])
'''

costs.sort()
left, right = 0, len(costs) - 1
while left <= right:
    mid = (left + right) // 2

    tmp = False
    visited = [False] * (n + 1)
    dfs(a, c, costs[mid])
    # print(costs[i], tmp)
    if tmp:
        right = mid - 1
        result = min(result, costs[mid])
    else:
        left = mid + 1

if result == 10 ** 11:
    result = -1
print(result)
