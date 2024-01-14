N, M = map(int, input().split())

result = -1

for _ in range(N):
    data = list(map(int, input().split()))
    result = max(result, min(data))

print(result)

"""
3 3
3 1 2
4 1 4
2 2 2

2 4
7 3 1 8
3 3 3 4
"""
