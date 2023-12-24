N, M, K = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

first = data[N - 1]
second = data[N - 2]

cnt = 0
result1 = 0

for i in range(M):
    if cnt == K:
        result1 += second
        cnt = 0
    else:
        result1 += first
        cnt += 1

print(result1)

result2 = (M // (K + 1)) * (first * K + second) + (M % (K + 1)) * first

print(result2)

"""
5 8 3
2 4 5 4 6
"""
