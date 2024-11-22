import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

dp1 = [0 for _ in range(n)]
dp2 = [0 for _ in range(n)]

answer = 0

for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)
        if A[n - 1 - j] < A[n - 1 - i]:
            dp2[n - 1 - i] = max(dp2[n - 1 - i], dp2[n - 1 - j] + 1)

for i in range(n):
    answer = max(answer, dp1[i] + dp2[i] + 1)

print(answer)