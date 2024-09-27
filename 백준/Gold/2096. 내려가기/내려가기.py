import sys

input = sys.stdin.readline

n = int(input())
max_dp = min_dp = list(map(int, input().split()))

for _ in range(n - 1):
    n0, n1, n2 = map(int, input().split())

    temp_max_0 = max(n0 + max_dp[0], n0 + max_dp[1])
    temp_min_0 = min(n0 + min_dp[0], n0 + min_dp[1])
    temp_max_1 = max(n1 + max_dp[0], n1 + max_dp[1], n1 + max_dp[2])
    temp_min_1 = min(n1 + min_dp[0], n1 + min_dp[1], n1 + min_dp[2])
    temp_max_2 = max(n2 + max_dp[2], n2 + max_dp[1])
    temp_min_2 = min(n2 + min_dp[2], n2 + min_dp[1])

    max_dp = [temp_max_0, temp_max_1, temp_max_2]
    min_dp = [temp_min_0, temp_min_1, temp_min_2]

print(max(max_dp), min(min_dp))