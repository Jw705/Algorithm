import sys

input = sys.stdin.readline

n, k = map(int, input().split())

data = []
use_room_info = [[0, 0] for _ in range(k)]

for _ in range(n):
    s, e = map(int, input().split())
    data.append([s, e])

data.sort(key=lambda x: x[1])
result = 0

for s, e in data:
    for i in range(k):
        if use_room_info[i][1] < s:
            use_room_info[i] = [s, e]
            use_room_info.sort(key=lambda x: x[1], reverse=True)
            result += 1
            break

print(result)