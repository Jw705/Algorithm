import sys

input = sys.stdin.readline

n, r, c = map(int, input().split())

cnt = 0


def z(x, y):
    global cnt
    if (x == r or x + 1 == r) and (y == c or y + 1 == c):
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        elif x + 1 == r and y + 1 == c:
            print(cnt + 3)
        sys.exit()
    else:
        cnt = cnt + 4


def f(x, y, l):
    if x + (l - 1) < r or y + (l - 1) < c:
        global cnt
        cnt += l * l
    elif l == 2:
        z(x, y)
    else:
        f(x, y, l // 2)
        f(x, y + l // 2, l // 2)
        f(x + l // 2, y, l // 2)
        f(x + l // 2, y + l // 2, l // 2)


f(0, 0, 2 ** n)