import sys

input = sys.stdin.readline

n, c = map(int, input().split())
a = b = n

for _ in range(c):
    x, y = map(int, input().split())
    if x >= a or y >= b:
        continue
    else:
        가로베기 = a * y
        세로베기 = x * b
        if 가로베기 > 세로베기:
            b = y
        else:
            a = x

print(a * b)