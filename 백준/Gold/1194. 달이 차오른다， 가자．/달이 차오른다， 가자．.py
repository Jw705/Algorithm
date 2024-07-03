import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, visited, start):
    startX, startY = start
    queue = deque([[startX, startY, 0, 0, 0, 0, 0, 0]])
    visited[startX][startY][0][0][0][0][0][0] = 0

    while queue:
        x, y, a, b, c, d, e, f = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif visited[nx][ny][a][b][c][d][e][f] == -1:

                # 출구 만나면 이동거리 반환
                if graph[nx][ny] == '1':
                    visited[nx][ny][a][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                    return visited[nx][ny][a][b][c][d][e][f]

                # 키 만나면
                elif graph[nx][ny] in ['a', 'b', 'c', 'd', 'e', 'f']:
                    if graph[nx][ny] == 'a':
                        visited[nx][ny][1][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                        queue.append([nx, ny, 1, b, c, d, e, f])
                    elif graph[nx][ny] == 'b':
                        visited[nx][ny][a][1][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                        queue.append([nx, ny, a, 1, c, d, e, f])
                    elif graph[nx][ny] == 'c':
                        visited[nx][ny][a][b][1][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                        queue.append([nx, ny, a, b, 1, d, e, f])
                    elif graph[nx][ny] == 'd':
                        visited[nx][ny][a][b][c][1][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                        queue.append([nx, ny, a, b, c, 1, e, f])
                    elif graph[nx][ny] == 'e':
                        visited[nx][ny][a][b][c][d][1][f] = visited[x][y][a][b][c][d][e][f] + 1
                        queue.append([nx, ny, a, b, c, d, 1, f])
                    elif graph[nx][ny] == 'f':
                        visited[nx][ny][a][b][c][d][e][1] = visited[x][y][a][b][c][d][e][f] + 1
                        queue.append([nx, ny, a, b, c, d, e, 1])

                # 문을 만나면
                elif graph[nx][ny] in ['A', 'B', 'C', 'D', 'E', 'F']:
                    visited[nx][ny][a][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                    # 그 문에 맞는 열쇠가 있을 때만 해당 좌표를 큐에 추가
                    if ((graph[nx][ny] == 'A' and a == 1) or (graph[nx][ny] == 'B' and b == 1) or (
                            graph[nx][ny] == 'C' and c == 1)
                            or (graph[nx][ny] == 'D' and d == 1) or (graph[nx][ny] == 'E' and e == 1) or (
                                    graph[nx][ny] == 'F' and f == 1)):
                        queue.append([nx, ny, a, b, c, d, e, f])

                elif graph[nx][ny] == '.':
                    queue.append([nx, ny, a, b, c, d, e, f])
                    visited[nx][ny][a][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1


n, m = map(int, input().split())
graph = []
visited = [[[[[[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(2)]
               for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(m)] for _ in range(n)]

minsik_locate = [0, 0]

for i in range(n):
    data = list(input())
    if '0' in data:
        minsik_locate = [i, data.index('0')]
        data[data.index('0')] = '.'
    graph.append(data)

result = bfs(graph, visited, minsik_locate)

if result == None:
    print(-1)
else:
    print(result)