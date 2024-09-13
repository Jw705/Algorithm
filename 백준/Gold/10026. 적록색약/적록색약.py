import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
visited_normal = [[False for _ in range(n)] for _ in range(n)]
visited_colorblind = [[False for _ in range(n)] for _ in range(n)]

for _ in range(n):
    graph.append(input().rstrip())


def bfs(x, y, is_colorblind, visited):
    area_color = graph[x][y]
    queue = deque([[x, y]])
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n and not visited[nx][ny]:
                if graph[nx][ny] == area_color:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                if is_colorblind and graph[nx][ny] != 'B' and area_color != 'B':
                    queue.append([nx, ny])
                    visited[nx][ny] = True


answer = [0, 0]

for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            bfs(i, j, False, visited_normal)
            answer[0] += 1
        if not visited_colorblind[i][j]:
            bfs(i, j, True, visited_colorblind)
            answer[1] += 1

print(answer[0], answer[1])