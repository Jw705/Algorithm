import sys

input = sys.stdin.readline

n = int(input())

answer = 0
while n > 0:
    tmp = n % 10
    if tmp == 0:
        n = n // 10
        i = 1
        while tmp == 0:
            tmp = (n % 10) * (10 ** i)
            n = n // 10
            i += 1
        answer += tmp
    else:
        answer += n % 10
        n = n // 10

print(answer)