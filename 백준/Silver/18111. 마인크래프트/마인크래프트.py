import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

data = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)


def findTime(n):
    time = 0
    block = 0
    for line in data:
        for d in line:
            if d > n:
                time += ((d - n) * 2)
                block += (d - n)
            elif d < n:
                time += (n - d)
                block -= (n - d)
    return time, block


answer_time = 1e9
answer_level = 0

for i in range(257):
    time, block = findTime(i)
    if b + block >= 0:
        if time <= answer_time:
            answer_time = time
            answer_level = i

print(answer_time, answer_level)