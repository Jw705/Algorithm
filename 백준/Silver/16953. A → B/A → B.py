import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().split())


def bfs():
    queue = deque([[A, 1]])
    while queue:
        n, cnt = queue.popleft()
        calc1 = n * 2
        calc2 = n * 10 + 1

        if calc1 == B or calc2 == B:
            print(cnt + 1)
            return

        if calc1 <= B:
            queue.append([calc1, cnt + 1])
        if calc2 <= B:
            queue.append([calc2, cnt + 1])
    print(-1)


bfs()