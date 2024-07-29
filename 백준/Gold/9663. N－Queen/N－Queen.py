import sys

input = sys.stdin.readline

n = int(input())
result = 0
board = [0] * n


def is_safe(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == abs(x - i):
            return False

    return True


def n_queens(x):
    if x == n:
        global result
        result += 1
        return

    for y in range(n):
        board[x] = y
        if is_safe(x):
            n_queens(x + 1)


n_queens(0)

print(result)