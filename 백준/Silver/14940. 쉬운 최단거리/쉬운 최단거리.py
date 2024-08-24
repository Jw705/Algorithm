import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
targetX, targetY = 0, 0

graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        targetX = i
        targetY = tmp.index(2)
    graph.append(tmp)

visited = [[-1 for _ in range(m)] for _ in range(n)]
visited[targetX][targetY] = 0


def bfs(startX, startY):
    queue = deque([[startX, startY]])

    while queue:
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif visited[nx][ny] == -1 and graph[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1


bfs(targetX, targetY)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            visited[i][j] = 0
        print(visited[i][j], end=' ')
    print()