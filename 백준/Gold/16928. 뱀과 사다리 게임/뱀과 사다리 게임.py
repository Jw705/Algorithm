import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [-1 for _ in range(101)]
dp = [101 for _ in range(101)]

for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

stack = [[1, 0]]

while stack:
    locate, distance = stack.pop()
    if board[locate] != -1:
        new_locate = board[locate]
        if dp[new_locate] > distance:
            dp[new_locate] = distance
            stack.append([new_locate, distance])
    else:
        for i in range(1, 7):
            new_locate = locate + i
            if new_locate <= 100 and dp[new_locate] > distance + 1:
                dp[new_locate] = distance + 1
                stack.append([new_locate, distance + 1])

print(dp[100])