def solution(x, y, n):
    INF = 1000001
    dp = [INF] * (y+1)
    dp[x] = 0
    
    for i in range(x+1,y+1):
        if i%2==0 and dp[i//2]!=INF:
            dp[i] = min(dp[i//2]+1, dp[i])
        if i%3==0 and dp[i//3]!=INF:
            dp[i] = min(dp[i//3]+1, dp[i])
        if i>n and dp[i-n]>=0:
            dp[i] = min(dp[i-n]+1, dp[i])
    
    if dp[y]==INF:
        return -1
    else:
        return dp[y]