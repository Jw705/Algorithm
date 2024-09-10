import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())

    answer = x
    b = (x - 1) % n + 1  # 'x' 해에 맞는 'b' 값 계산

    while answer <= m * n:
        if b == y:  # 목표 연도 도달
            print(answer)
            break
        answer += m
        b = (b + m - 1) % n + 1
    else:
        print(-1)