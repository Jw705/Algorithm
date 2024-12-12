def solution(temperature, t1, t2, a, b, onboard):
    n = len(onboard)
    INF = int(1e9)
    
    temperature += 10
    t1 += 10
    t2 += 10
        
    # dp[i][j] : i분에 j + 10도를 만들 수 있는 최소 전력
    dp = [[INF for _ in range(51)] for _ in range(1001)]
    dp[0][temperature] = 0
    
    # time에 temp가 유효한 온도 범위안에 있는지 확인
    def is_valid(time, temp):
        return onboard[time] == 0 or (t1 <= temp <= t2)
    
    for i in range(n - 1):
        for j in range(51):
            if dp[i][j] == INF: 
                continue           
                
            # 에어컨 on (전력 소비)
            if j < 50 and is_valid(i + 1, j + 1):
                dp[i + 1][j + 1] = min(dp[i][j] + a, dp[i + 1][j + 1]) # 온도 1 상승 -> 전력 a 소비
            if j > 0 and is_valid(i + 1, j - 1):
                dp[i + 1][j - 1] = min(dp[i][j] + a, dp[i + 1][j - 1]) # 온도 1 하강 -> 전력 a 소비
            if t1 <= j <= t2 and is_valid(i + 1, j):
                dp[i + 1][j] = min(dp[i][j] + b, dp[i + 1][j]) # 희망 온도와 동일 -> 온도 유지, 전력 b 소비

            # 에어컨 off (전력 소비 X)                        
            if j < temperature and is_valid(i + 1, j + 1):
                dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j + 1]) # 실외 온도보다 낮다 -> 온도 1 상승         
            elif j == temperature and is_valid(i + 1, j):
                dp[i + 1][j] = min(dp[i][j], dp[i + 1][j]) # 실외 온도와 같다 -> 온도 유지            
            elif j > temperature and is_valid(i + 1, j - 1):
                dp[i + 1][j - 1] = min(dp[i][j], dp[i + 1][j - 1]) # 실외 온도보다 높다 -> 온도 1 하강
                        
    return min(dp[n - 1])