n = int(input())

data = []

for _ in range(n):
    name, score = input().split()
    data.append([name, int(score)])

data.sort(key=lambda data: data[1])

for d in data:
    print(d[0], end=' ')

'''
2
홍길동 95
이순신 77
'''