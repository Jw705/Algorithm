import sys

input = sys.stdin.readline

n = int(input())

data = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

visited = [[False for _ in range(n)] for _ in range(n)]


def serach_square(n, a, b):
    tmp = 0
    for i in range(a, a + n):
        for j in range(b, b + n):
            tmp += data[i][j]
    if tmp == 0:
        return 'white'
    elif tmp == n * n:
        return 'blue'
    else:
        return 'none'


def visit_square(n, a, b):
    for i in range(a, a + n):
        for j in range(b, b + n):
            visited[i][j] = True


white = 0
blue = 0
l = n

while l >= 1:
    for i in range(0, n, l):
        for j in range(0, n, l):
            if not visited[i][j]:
                res = serach_square(l, i, j)
                if res == 'white':
                    white += 1
                    visit_square(l, i, j)
                elif res == 'blue':
                    blue += 1
                    visit_square(l, i, j)
    l = l // 2

print(white)
print(blue)