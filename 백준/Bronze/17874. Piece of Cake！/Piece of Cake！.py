import sys

input = sys.stdin.readline

n, h, v = map(int, input().split())

ans = max(h * v * 4, (n - h) * v * 4, h * (n - v) * 4, (n - h) * (n - v) * 4)

print(ans)