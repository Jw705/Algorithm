import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [False] * 100001

queue = deque([[n, 0]])
visited[n] = True

while queue:
    v, sec = queue.popleft()
    if v == k:
        print(sec)
        break
    for i in [2 * v, v + 1, v - 1]:
        if 0 <= i <= 100000 and not visited[i]:
            queue.append([i, sec + 1])
            visited[i] = True