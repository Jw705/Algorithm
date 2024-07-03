import sys
from collections import deque

input = sys.stdin.readline

minsik_keys = []


def bfs(graph, visited, start, target):
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
                # 출구 만나면 무조건 좌표 반환
                if graph[nx][ny] == '1':
                    visited[nx][ny][a][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                    #print('도착', visited[nx][ny][a][b][c][d][e][f])
                    #print('키는', a, b, c, d, e, f)
                    return visited[nx][ny][a][b][c][d][e][f]
                # 키나 만나면
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
                # 문 만나면
                elif graph[nx][ny] in ['A', 'B', 'C', 'D', 'E', 'F']:
                    visited[nx][ny][a][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1
                    if graph[nx][ny] == 'A' and a == 1:
                        queue.append([nx, ny, a, b, c, d, e, f])
                    elif graph[nx][ny] == 'B' and b == 1:
                        queue.append([nx, ny, a, b, c, d, e, f])
                    elif graph[nx][ny] == 'C' and c == 1:
                        queue.append([nx, ny, a, b, c, d, e, f])
                    elif graph[nx][ny] == 'D' and d == 1:
                        queue.append([nx, ny, a, b, c, d, e, f])
                    elif graph[nx][ny] == 'E' and e == 1:
                        queue.append([nx, ny, a, b, c, d, e, f])
                    elif graph[nx][ny] == 'F' and f == 1:
                        queue.append([nx, ny, a, b, c, d, e, f])

                elif graph[nx][ny] == '.':
                    queue.append([nx, ny, a, b, c, d, e, f])
                    visited[nx][ny][a][b][c][d][e][f] = visited[x][y][a][b][c][d][e][f] + 1


n, m = map(int, input().split())
graph = []
visited = [[[[[[[[-1 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(
    2)] for _ in range(2)] for _ in range(2)] for _ in range(m)] for _ in range(n)]

minsik_locate = [0, 0]

for i in range(n):
    data = list(input())
    if '0' in data:
        minsik_locate = [i, data.index('0')]
        data[data.index('0')] = '.'
    graph.append(data)

target = '1'

result = bfs(graph, visited, minsik_locate, target)

if result == None:
    print(-1)
else:
    print(result)

'''
n,m은 <50 이하이므로 dfs 여러번 사용해도 된다고 판단.

1) dfs 한번 수행해서
    1. 1에 도달 가능 여부 체크
    2. 도달 가능한열쇠 종류, 문 종류 list에 추가
2) 1에 도달 못하면
    1. 열수 있는 문 체크 (키 있는거 우선, 키 없으면 열쇠 가까운거 우선)
    2. 열수 잇는 문 중에거 (가장 가까운) 키 찾고, 열쇠로 간다.

3) 1에 도달 못하면
    1. 열 수 있는 문 체크 (현재 키가 있는거)
    2. 열 수 있는 문이 없으면 일단 가까운 키부터 먹는다?

1 7
0..aA.1

'''
