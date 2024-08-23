import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

visited = [0] * 1000001


def bfs(x, y):
    queue = deque([x])
    visited[x] = 1

    while queue:
        v = queue.popleft()
        if v == y:
            return visited[v]

        for i in (2 * v, v - 1, v + 1):
            if 0 <= i <= 100001 and visited[i] == 0:
                if i == 2 * v:
                    visited[i] = visited[v]
                else:
                    visited[i] = visited[v] + 1
                queue.append(i)


bfs(n, k)
print(visited[k] - 1)