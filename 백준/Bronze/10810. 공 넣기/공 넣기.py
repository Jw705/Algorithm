import sys

input = sys.stdin.readline

n, m = map(int, input().split())
data = [0] * (n + 1)

for _ in range(m):
    i, j, k = map(int, input().split())
    for a in range(i, j + 1):
        data[a] = k

for d in range(1, n + 1):
    print(data[d], end=' ')