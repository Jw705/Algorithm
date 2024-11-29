def solution(board, skill):
    n, m = len(board), len(board[0])
    # 누적합 배열 생성
    acc = [[0] * (m + 1) for _ in range(n + 1)]

    # skill 적용
    for type_, r1, c1, r2, c2, degree in skill:
        if type_ == 1:  # 공격일 경우
            degree = -degree
        # 누적합 방식으로 시작점과 끝점 설정
        acc[r1][c1] += degree
        acc[r1][c2 + 1] -= degree
        acc[r2 + 1][c1] -= degree
        acc[r2 + 1][c2 + 1] += degree

    # 누적합 적용 (행 기준)
    for i in range(n):
        for j in range(m):
            acc[i][j + 1] += acc[i][j]

    # 누적합 적용 (열 기준)
    for j in range(m):
        for i in range(n):
            acc[i + 1][j] += acc[i][j]

    # 결과 계산
    answer = 0
    for i in range(n):
        for j in range(m):
            board[i][j] += acc[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer
