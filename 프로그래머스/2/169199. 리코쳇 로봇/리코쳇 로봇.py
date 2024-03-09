from collections import deque


def bfs(board, start, visited):
    queue = deque([[start[0], start[1], 0]])
    visited[start[0]][start[1]] = True
    
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    while queue:
        v = queue.popleft()
        for direction in directions:
            dx, dy = direction
            nx, ny, c = v
            while (0 <= nx + dx < len(board) and 0 <= ny + dy < len(board[0])
                   and board[nx + dx][ny + dy] != 'D'):
                nx += dx
                ny += dy

            if board[nx][ny] == 'G':
                return c + 1
            elif not visited[nx][ny]:
                queue.append([nx, ny, c + 1])
                visited[nx][ny] = True
    return -1


def solution(board):
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    start = [0, 0]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                start = [i, j]
                break

    answer = bfs(board, start, visited)
    return answer