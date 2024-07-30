import sys
input = sys.stdin.readline

t = int(input())
p = [0] * 101
p[1] = 1
p[2] = 1
for i in range(3, 101):
    p[i] = p[i - 2] + p[i - 3]

for _ in range(t):
    n = int(input())
    print(p[n])