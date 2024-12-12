def solution(temperature, t1, t2, a, b, onboard):
    answer = 0
    n = len(onboard)
    
    temperature += 10
    t1 += 10
    t2 += 10
    
    # DP[i][j] : i분에 j + 10 온도를 만들 수 있는 가장 적은 전력
    dp = [[int(1e9) for _ in range(51)] for _ in range(1001)]
    dp[0][temperature] = 0
    
    for i in range(n - 1):
        for j in range(51):
            if dp[i][j] != int(1e9):                  
                
                # 에어컨 on                
                # 희망 온도보다 낮다 -> 온도 1 상승, 전력 a 소비
                if j < 50:
                    if onboard[i + 1] == 0 or (onboard[i + 1] == 1 and t1 <= j + 1 <= t2):
                        dp[i + 1][j + 1] = min(dp[i][j] + a, dp[i + 1][j + 1])
                # 희망 온도보다 높다 -> 온도 1 하강, 전력 a 소비
                if j > 0:
                    if onboard[i + 1] == 0 or (onboard[i + 1] == 1 and t1 <= j - 1 <= t2):
                        dp[i + 1][j - 1] = min(dp[i][j] + a, dp[i + 1][j - 1]) 
                # 희망 온도 내에 있다 -> 온도 유지, 전력 b 소비
                if t1 <= j <= t2:
                    if onboard[i + 1] == 0 or (onboard[i + 1] == 1 and t1 <= j <= t2):
                        dp[i + 1][j] = min(dp[i][j] + b, dp[i + 1][j])
                    
                
                # 에어컨 off (전력 소비 X)
                # 실외 온도보다 낮다 -> 온도 1 상승
                if j < temperature:
                    if onboard[i + 1] == 0 or (onboard[i + 1] == 1 and t1 <= j + 1 <= t2):
                        dp[i + 1][j + 1] = min(dp[i][j], dp[i + 1][j + 1])
                # 실외 온도와 같다 -> 유지
                elif j == temperature:
                    if onboard[i + 1] == 0 or (onboard[i + 1] == 1 and t1 <= j <= t2):
                        dp[i + 1][j] = min(dp[i][j], dp[i + 1][j])
                # 실외 온도보다 높다 -> 온도 1 하강
                elif j > temperature:
                    if onboard[i + 1] == 0 or (onboard[i + 1] == 1 and t1 <= j - 1 <= t2):
                        dp[i + 1][j - 1] = min(dp[i][j], dp[i + 1][j - 1])
                        
    answer = min(dp[n - 1])
    
    return answer