import sys
from collections import deque

input = sys.stdin.readline

n, c = map(int, input().split())
m = int(input())

truck = deque()
box_info = []
capacity_info = [0] * (n + 1)

for _ in range(m):
    보내는마을번호, 받는마을번호, 박스개수 = map(int, input().split())
    box_info.append([보내는마을번호, 받는마을번호, 박스개수])

box_info.sort(key=lambda x: x[1])
result = 0

for box in box_info:
    보내는마을번호, 받는마을번호, 박스개수 = box
    배송할개수 = 박스개수
    for i in range(보내는마을번호, 받는마을번호):
        if c - capacity_info[i] < 배송할개수:
            배송할개수 = c - capacity_info[i]
        capacity_info[i] += 배송할개수
    result += 배송할개수

print(result)