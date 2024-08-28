import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
queue = deque()
visited = [[False for _ in range(m)] for _ in range(n)]

for i in range(n):
    tmp = input().rstrip()
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 'I':
            queue.append((i, j))
            visited[i][j] = True

answer = 0
while queue:
    x, y = queue.popleft()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        elif not visited[nx][ny] and graph[nx][ny] != 'X':
            queue.append([nx, ny])
            visited[nx][ny] = True
            if graph[nx][ny] == 'P':
                answer += 1

if answer == 0:
    print('TT')
else:
    print(answer)