N, K = map(int, input().split())

result = 0

while N > 1:
    if N % K == 0:
        result += 1
        N = N // K
    else:
        N -= 1
        result += 1

print(result)

"""
25 5
"""
