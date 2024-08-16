import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []
for _ in range(n):
    tmp = input().rstrip()
    graph.append(tmp)

visited = [[0 for _ in range(n)] for _ in range(n)]


def bfs(startX, startY):
    queue = deque([[startX, startY]])
    visited[startX][startY] = 1

    house_cnt = 1

    while queue:
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif visited[nx][ny] == 0 and graph[nx][ny] == '1':
                queue.append([nx, ny])
                visited[nx][ny] = True
                house_cnt += 1

    return house_cnt


answer = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == '1' and not visited[i][j]:
            answer.append(bfs(i, j))

answer.sort()

print(len(answer))
for a in answer:
    print(a)