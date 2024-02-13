import sys

input = sys.stdin.readline

cnt = 0
f = [0] * 4000


def fibonacci(n):
    global cnt
    f[1] = 1
    f[2] = 1
    for i in range(3, n + 1):
        cnt += 1
        f[i] = f[i - 1] + f[i - 2]
    return f[n]


n = int(input())
fibonacci(n)

print(f[n], cnt)