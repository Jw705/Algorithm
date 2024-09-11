import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())
visited = []


def bfs():
    queue = deque([[A, 1]])
    while queue:
        n, cnt = queue.popleft()
        calc1 = n * 2
        calc2 = n * 10 + 1

        if calc1 == B or calc2 == B:
            print(cnt + 1)
            return

        if calc1 <= B and not (calc1 in visited):
            queue.append([calc1, cnt + 1])
            visited.append(calc1)
        if calc2 <= B and not (calc2 in visited):
            queue.append([calc2, cnt + 1])
            visited.append(calc2)
    print(-1)


bfs()