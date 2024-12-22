def solution(target):
    MAX = target + 1
    dp = [MAX] * (target) + [0]
    dp2 = [0] * (target) + [0]
    
    for i in range(target, -1, -1):
        # 불
        if i >= 50:
            j = 50
            if dp[i - j] > dp[i] + 1:
                dp[i - j] = dp[i] + 1
                dp2[i - j] = dp2[i] + 1
            if dp[i - j] == dp[i] + 1:
                dp2[i - j] = max(dp2[i - j], dp2[i] + 1)   
        
        for j in range(1, 21):
            # 싱글
            if i >= j:
                if dp[i - j] > dp[i] + 1:
                    dp[i - j] = dp[i] + 1
                    dp2[i - j] = dp2[i] + 1
                if dp[i - j] == dp[i] + 1:
                    dp2[i - j] = max(dp2[i - j], dp2[i] + 1)         
            # 더블
            if i >= j * 2:
                if dp[i - (j * 2)] > dp[i] + 1:
                    dp[i - (j * 2)] = dp[i] + 1            
                    dp2[i - (j * 2)] = dp2[i] 
                if dp[i - (j * 2)] == dp[i] + 1:        
                    dp2[i - (j * 2)] = max(dp2[i - (j * 2)], dp2[i])
            # 트리플
            if i >= j * 3:
                if dp[i - (j * 3)] > dp[i] + 1:
                    dp[i - (j * 3)] = dp[i] + 1            
                    dp2[i - (j * 3)] = dp2[i] 
                if dp[i - (j * 3)] == dp[i] + 1:        
                    dp2[i - (j * 3)] = max(dp2[i - (j * 3)], dp2[i])
    
    answer = [dp[0], dp2[0]]
    return answer