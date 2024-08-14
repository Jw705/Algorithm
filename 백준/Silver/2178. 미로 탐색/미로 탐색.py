import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
for _ in range(n):
    tmp = input().rstrip()
    graph.append(tmp)

visited = [[0 for _ in range(m)] for _ in range(n)]


def bfs(startX, startY):
    queue = deque([[startX, startY]])
    visited[startX][startY] = 1

    while queue:
        x, y = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y]

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif visited[nx][ny] == 0 and graph[nx][ny] == '1':
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

    return 1e9


result = bfs(0, 0)

if result == 1e9:
    print(-1)
else:
    print(result)