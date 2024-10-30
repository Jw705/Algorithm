import sys

input = sys.stdin.readline

r, c = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(r)]
answer = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0 for _ in range(c)] for _ in range(r)]


def dfs():
    global answer

    stack = [[0, 0, graph[0][0]]]
    while stack:
        x, y, route = stack.pop()
        answer = max(answer, len(route))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if not graph[nx][ny] in route:
                    stack.append([nx, ny, route + graph[nx][ny]])


dfs()
print(answer)
