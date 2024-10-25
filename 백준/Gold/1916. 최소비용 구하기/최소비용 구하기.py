import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for i in range(m):
    origin, destination, cost = map(int, input().split())
    graph[origin].append((destination, cost))

a, b = map(int, input().split())


def dijkstra(start):
    visited = [int(1e9)] * (n + 1)
    visited[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if visited[now] < dist:
            continue

        for info in graph[now]:
            destination, cost = info
            updated_dist = dist + cost

            if updated_dist < visited[destination]:
                visited[destination] = updated_dist
                heapq.heappush(q, (updated_dist, destination))

    return visited

print(dijkstra(a)[b])