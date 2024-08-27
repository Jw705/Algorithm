import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

graph = []
queue = deque()
visited = [[[1e9 for _ in range(h)] for _ in range(m)] for _ in range(n)]

for k in range(h):
    tmp_graph = []
    for i in range(n):
        tmp = list(map(int, input().split()))
        tmp_graph.append(tmp)
        for j in range(m):
            if tmp[j] == 1:
                queue.append((i, j, k))  # 1인 모든 위치를 큐에 추가
                visited[i][j][k] = 0
    graph.append(tmp_graph)


while queue:
    x, y, z = queue.popleft()

    dx = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m or nz < 0 or nz >= h:
            continue
        elif visited[nx][ny][nz] > visited[x][y][z] + 1 and graph[nz][nx][ny] == 0:
            queue.append([nx, ny, nz])
            visited[nx][ny][nz] = visited[x][y][z] + 1

max_value = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == -1:
                visited[i][j][k] = -1
            else:
                max_value = max(max_value, visited[i][j][k])

if max_value == 1e9:
    print(-1)
else:
    print(max_value)
