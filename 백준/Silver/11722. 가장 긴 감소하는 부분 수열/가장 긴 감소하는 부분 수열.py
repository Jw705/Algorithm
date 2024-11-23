import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if A[n - 1 - j] < A[n - 1 - i]:
            dp[n - 1 - i] = max(dp[n - 1 - i], dp[n - 1 - j] + 1)

print(max(dp) + 1)