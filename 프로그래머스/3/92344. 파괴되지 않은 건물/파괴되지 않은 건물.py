def solution(board, skill):
    n, m = len(board), len(board[0])
    prifix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:
            degree *= -1
        prifix_sum[r1][c1] += degree
        prifix_sum[r1][c2 + 1] -= degree
        prifix_sum[r2 + 1][c1] -= degree
        prifix_sum[r2 + 1][c2 + 1] += degree
    
    for i in range(n):
        for j in range(m):
            prifix_sum[i][j + 1] += prifix_sum[i][j]
            
    for i in range(m):
        for j in range(n):
            prifix_sum[j + 1][i] += prifix_sum[j][i]
        
    answer = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + prifix_sum[i][j] > 0:
                answer += 1       
    
    return answer
