from collections import deque

n, m = map(int, input().split())

data = []

for _ in range(n):
    data.append(list(map(int, input())))


def bfs(graph, x, y):
    queue = deque([x, y])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    length = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append([dx, dy])

    return graph


print(bfs(data, 0, 0))
