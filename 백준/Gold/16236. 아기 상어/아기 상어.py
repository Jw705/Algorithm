import sys
from collections import deque

def bfs(graph, start, visited, size):
    startX, startY = start
    queue = deque([[startX, startY]])
    visited[startX][startY] = 0

    pos_list = []

    while queue:
        x, y = queue.popleft()
        dx = [-1, 0, 0, 1]
        dy = [0, -1, 1, 0]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif visited[nx][ny] == -1:
                if graph[nx][ny] > size:
                    continue
                elif graph[nx][ny] == 0 or graph[nx][ny] == size:
                    queue.append([nx, ny])
                    visited[nx][ny] = visited[x][y] + 1
                elif graph[nx][ny] < size:
                    pos_list.append([nx, ny, visited[x][y] + 1])

    if pos_list:
        pos_list.sort(key=lambda x: (x[2], x[0], x[1]))
        return pos_list[0]


input = sys.stdin.readline

n = int(input())

space = []
visited = [[-1] * n for _ in range(n)]

baby_shark_locate = [-1, -1]
baby_shark_size = 2
baby_shark_eat = 0

for i in range(n):
    data = list(map(int, input().split()))
    if 9 in data:
        baby_shark_locate = [i, data.index(9)]
        data[data.index(9)] = 0
    space.append(data)


result = 0

while True:
    next_locate_data = bfs(space, baby_shark_locate, visited, baby_shark_size)
    if next_locate_data == None:
        break
    else:
        nx, ny, l = next_locate_data
        space[nx][ny] = 0
        baby_shark_locate = [nx, ny]

        result += l
        baby_shark_eat += 1
        if baby_shark_eat == baby_shark_size:
            baby_shark_size += 1
            baby_shark_eat = 0
        visited = [[-1] * n for _ in range(n)]

print(result)
