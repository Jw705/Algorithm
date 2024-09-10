import sys

# 입력 받기
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    a = 1
    b = 1
    answer = 1
    visited = [False] * (n + 1)
    while a < x:
        a += 1
        if b < n:
            b += 1
        else:
            b = 1
        answer += 1

    while True:
        isKaingCalendarEnd = a == m and b == n
        isTargetYear = a == x and b == y
        if isTargetYear:
            print(answer)
            break
        elif answer > m * n:
            print(-1)
            break
        else:

            b = (b + m) % n
            if b == 0:
                b = n
            answer += m