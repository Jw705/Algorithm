def dfs(depth):
    global answer
    if depth == int(change_cnt):
        answer = max(answer, int(''.join(board)))
        return
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            board[i], board[j] = board[j], board[i]
            check = int(''.join(board))
            if (depth, check) not in visited:
                visited.append((depth, check))
                dfs(depth + 1)

            board[i], board[j] = board[j], board[i]


T = int(input())

for test_case in range(1, T + 1):
    board, change_cnt = input().split()
    board = list(board)

    visited = []
    answer = 0
    dfs(0)
    print(f'#{test_case} {answer}')