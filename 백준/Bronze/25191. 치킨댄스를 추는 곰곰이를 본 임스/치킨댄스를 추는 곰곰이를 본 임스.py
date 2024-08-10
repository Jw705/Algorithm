import sys

input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())

answer = 0
while n > 0:
    if a >= 2:
        a -= 2
        n -= 1
        answer += 1
    elif b >= 1:
        b -= 1
        n -= 1
        answer += 1
    else:
        break

print(answer)