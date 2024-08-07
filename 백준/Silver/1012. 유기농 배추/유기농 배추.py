import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(board, visited, x, y):
    visited[x][y] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        elif not visited[nx][ny] and board[nx][ny] == 1:
            board[nx][ny] = 0
            dfs(board, visited, nx, ny)


t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                result += 1
                dfs(board, visited, i, j)
    print(result)