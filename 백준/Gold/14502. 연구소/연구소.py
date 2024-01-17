import sys
import copy
from collections import deque
from itertools import combinations

n, m = map(int, input().split())

input_graph = [[] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 입력을 받아 트리 생성
for i in range(n):
    input_graph[i] = list(map(int, sys.stdin.readline().split()))

empty = []

safe_size = 0

for i in range(n):
    for j in range(m):
        if input_graph[i][j] == 0:
            safe_size += 1
            empty.append([i, j])

wall_list = list(combinations(empty, 3))

max_safe_size = 0


def bfs(graph, x, y):
    queue = deque()
    queue.append((x, y))

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
                cnt += 1
    return cnt


for wall in wall_list:
    copied_graph = copy.deepcopy(input_graph)
    copied_graph[wall[0][0]][wall[0][1]] = 1
    copied_graph[wall[1][0]][wall[1][1]] = 1
    copied_graph[wall[2][0]][wall[2][1]] = 1

    for i in range(n):
        for j in range(m):
            if copied_graph[i][j] == 2:
                bfs(copied_graph, i, j)

    tmp = 0
    for i in range(n):
        for j in range(m):
            if copied_graph[i][j] == 0:
                tmp += 1
    max_safe_size = max(max_safe_size, tmp)

print(max_safe_size)

'''# 1번 노드부터 탐색 시작
bfs(1)

for i in range(1, n + 1):
    print(order[i])'''

'''
5 5 1
1 4
1 2
2 3
2 4
3 4
'''
