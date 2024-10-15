import sys

input = sys.stdin.readline

a, b, c = map(int, input().split())
answer = 1

while b > 0:
    if (b % 2) == 1:
        answer = answer * a % c
    b = b // 2
    a = a * a % c

print(answer)