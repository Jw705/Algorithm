import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(n)]

answer = 0

for i in range(n):
    dp[i] = A[i]
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + A[i])
            
print(max(dp))