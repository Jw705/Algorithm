# 80m

def solution(alp, cop, problems):
    target_alp, target_cop = [0, 0]  # 목표값

    for problem in problems:
        target_alp = max(target_alp, problem[0])
        target_cop = max(target_cop, problem[1])
    
    # dp[i][j] : (알고력 i, 코딩력 j) 상태에 도달하는 데 필요한 최단 시간
    dp = [[int(1e9) for _ in range(451)] for _ in range(451)]
    alp = min(alp, target_alp)
    cop = min(cop, target_cop)
    
    dp[alp][cop] = 0

    for i in range(alp, target_alp + 1):
        for j in range(cop, target_cop + 1):
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for problem in problems:
                alp_req, cop_req, alp_rwd, cop_rwd, cost = problem
                if i >= alp_req and j >= cop_req:
                    new_alp = min(i + alp_rwd, target_alp)
                    new_cop = min(j + cop_rwd, target_cop)
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)

    return dp[target_alp][target_cop]