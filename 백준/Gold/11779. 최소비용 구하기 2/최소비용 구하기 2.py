import sys
import heapq
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())

answer = []
graph = [[] for _ in range(n + 1)]

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

s, e = map(int, input().split())

path = [[] for _ in range(n + 1)]


def dijkstra(start):
    distance = [int(1e10)] * (n + 1)
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, cur_node = heapq.heappop(q)
        if distance[cur_node] < dist:
            continue
        else:
            for next_node, c in graph[cur_node]:
                cost = dist + c
                if cost < distance[next_node]:
                    path[next_node] = cur_node
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
    return distance


print(dijkstra(s)[e])

path2 = [e]
now = e
while now != s:
    now = path[now]
    path2.append(now)

path2.reverse()

print(len(path2))
print(' '.join(map(str, path2)))