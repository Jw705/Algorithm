import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline

n, m = map(int, input().split())
board = []

answer = 0

for _ in range(n):
    board.append(list(map(int, input().split())))


# ㅗ, ㅜ, ㅓ, ㅏ 모양 체크 함수
def check_special_shapes(x, y):
    global answer
    # ㅗ ㅜ ㅓ ㅏ 체크
    if 0 < x < n - 1 and y < m - 1:
        sum_ㅏ = board[x][y] + board[x - 1][y] + board[x + 1][y] + board[x][y + 1]
        answer = max(answer, sum_ㅏ)
    if 0 < x < n - 1 and 0 < y:
        sum_ㅓ = board[x][y] + board[x - 1][y] + board[x + 1][y] + board[x][y - 1]
        answer = max(answer, sum_ㅓ)
    if x < n - 1 and 0 < y < m - 1:
        sum_ㅜ = board[x][y] + board[x][y - 1] + board[x][y + 1] + board[x + 1][y]
        answer = max(answer, sum_ㅜ)
    if 0 < x and 0 < y < m - 1:
        sum_ㅗ = board[x][y] + board[x][y - 1] + board[x][y + 1] + board[x - 1][y]
        answer = max(answer, sum_ㅗ)


visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y, square_cnt, sum_num):
    global answer
    if square_cnt == 4:
        answer = max(answer, sum_num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True  # 방문처리
            dfs(nx, ny, square_cnt + 1, sum_num + board[nx][ny])
            visited[nx][ny] = False  # 방문처리 제거


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, board[i][j])
        visited[i][j] = False
        check_special_shapes(i, j)

print(answer)
