def solution(temperature, t1, t2, a, b, onboard):
    n = len(onboard)
    
    temperature += 10
    t1 += 10
    t2 += 10
    
    # DP[i][j] : i분에 j + 10 온도를 만들 수 있는 가장 적은 전력
    MAX = float('inf')
    dp = [[MAX for _ in range(51)] for _ in range(n)]
    dp[0][temperature] = 0
    
    def is_valid(temp, onboard_state):
        # 온도가 유효한 범위인지 확인
        return onboard_state == 0 or (t1 <= temp <= t2)
    
    for i in range(n - 1):
        for j in range(51):
            if dp[i][j] == MAX:
                continue
            
            # 에어컨 ON 케이스
            if j < 50 and is_valid(j + 1, onboard[i + 1]):
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j] + a)
            if j > 0 and is_valid(j - 1, onboard[i + 1]):
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j] + a)
            if is_valid(j, onboard[i + 1]):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + b)
            
            # 에어컨 OFF 케이스
            if j < temperature and is_valid(j + 1, onboard[i + 1]):
                dp[i + 1][j + 1] = min(dp[i + 1][j + 1], dp[i][j])
            if j == temperature and is_valid(j, onboard[i + 1]):
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
            if j > temperature and is_valid(j - 1, onboard[i + 1]):
                dp[i + 1][j - 1] = min(dp[i + 1][j - 1], dp[i][j])
    
    # 마지막 상태에서 최소 전력값 탐색
    return min(dp[n - 1])
