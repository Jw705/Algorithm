import sys
import heapq

input = sys.stdin.readline

n, d = map(int, input().split())
graph = [[] for _ in range(10001)]
for i in range(10000):
    graph[i].append([i + 1, 1])

for _ in range(n):
    s, e, dist = map(int, input().split())
    graph[s].append([e, dist])


def dijkstra(start):
    q = []
    distance = [int(1e9)] * (10001)
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if dist > distance[node]:
            continue
        for next_node, next_dist in graph[node]:
            new_dist = dist + next_dist
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(q, (new_dist, next_node))
    return distance


print(dijkstra(0)[d])