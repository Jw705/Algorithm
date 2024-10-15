import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
answer = 1

def power(b):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    if b % 2 == 0:
        return power(b // 2) ** 2 % c
    else:
        return power(b // 2) ** 2 * a % c

print(power(b))