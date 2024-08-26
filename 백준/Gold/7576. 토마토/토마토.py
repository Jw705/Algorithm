from collections import deque

m, n = map(int, input().split())

graph = []
queue = deque()

# 그래프 입력과 동시에 초기 큐 설정
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            queue.append((i, j))  # 1인 모든 위치를 큐에 추가

# 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 탐색
while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

# 최대값 계산
max_value = 0
for row in graph:
    max_value = max(max_value, max(row))

# 결과 출력
if any(0 in row for row in graph):
    print(-1)
else:
    print(max_value - 1)