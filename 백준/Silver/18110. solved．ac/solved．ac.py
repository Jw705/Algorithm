import sys

input = sys.stdin.readline

n = int(input())
if n == 0:
    print(0)
else:
    data = []
    for _ in range(n):
        data.append(int(input()))

    data.sort()
    fifteen_percent = int(n * 0.15 + 0.5)
    print(int(sum(data[fifteen_percent:n - fifteen_percent]) / (n - 2 * fifteen_percent) + 0.5))