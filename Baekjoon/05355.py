N = int(input())

for _ in range(N):
    data = list(input().split())
    res = float(data[0])
    for i in range(1, len(data)):
        if data[i] == "@":
            res *= 3
        elif data[i] == "%":
            res += 5
        elif data[i] == "#":
            res -= 7
    print(f'{round(res, 3):.2f}')

"""
3
3 @ %
10.4 # % @
8 #
"""
