def solution(n, tops):
    dp1 = [2 + tops[0]] + [0] * (n - 1)
    dp2 = [1] + [0] * (n - 1)
    for i in range(1, len(tops)):
        dp1[i] = (dp1[i - 1] * (2 + tops[i]) + dp2[i - 1] * (1 + tops[i])) % 10007
        dp2[i] = (dp2[i - 1] + dp1[i - 1]) % 10007    
    return (dp1[-1] + dp2[-1]) % 10007