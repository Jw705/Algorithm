import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    m = int(input())
    옷장 = {}
    for _ in range(m):
        의상이름, 의상종류 = input().split()
        if 의상종류 in 옷장:
            옷장[의상종류] += 1
        else:
            옷장[의상종류] = 1

    result = 1
    for count in 옷장.values():
        result *= (count + 1)

    result -= 1
    print(result)