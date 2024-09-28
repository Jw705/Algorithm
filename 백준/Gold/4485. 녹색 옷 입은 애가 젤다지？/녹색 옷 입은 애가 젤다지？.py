import sys
import heapq

input = sys.stdin.readline

n = int(input())
problem_count = 1

while n != 0:
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    dist = [[int(1e9) for _ in range(n)] for _ in range(n)]
    q = []
    heapq.heappush(q, (0, 0, graph[0][0]))
    dist[0][0] = graph[0][0]
    while q:
        x, y, distance = heapq.heappop(q)
        if dist[x][y] < distance:
            continue
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] > distance + graph[nx][ny]:
                dist[nx][ny] = distance + graph[nx][ny]
                heapq.heappush(q, (nx, ny, distance + graph[nx][ny]))

    print(f"Problem {problem_count}: {dist[n - 1][n - 1]}")
    problem_count += 1
    n = int(input())