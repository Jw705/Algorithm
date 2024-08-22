import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 100001

queue = deque([[n, 0]])

answer = 1e9
answer_cnt = 0

while queue:
    v, sec = queue.popleft()
    if v == k:
        if sec < answer:
            answer = sec
            answer_cnt = 1
        elif sec == answer:
            answer_cnt += 1
    if sec < answer:
        for i in [2 * v, v + 1, v - 1]:
            if 0 <= i <= 100000 and (visited[i] == 0 or visited[i] == sec + 1):
                queue.append([i, sec + 1])
                visited[i] = sec + 1

print(answer)
print(answer_cnt)