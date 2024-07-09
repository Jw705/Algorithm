import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, visited, start):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True


n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, visited, 1)

result = 0
for v in visited:
    if v == True:
        result += 1

print(result - 1)
