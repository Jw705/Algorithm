import sys
import heapq
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
while n != 0 and m != 0:
    s, d = map(int, input().split())

    graph = [[] for _ in range(n)]
    prev_node = [[] for _ in range(n)]

    for i in range(m):
        u, v, p  = map(int, input().split())
        graph[u].append((v, p))


    def dijkstra(start):
        distance = [int(1e10)] * (n)
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
                        prev_node[next_node].clear()
                        prev_node[next_node].append([cur_node,(next_node, c)])
                        distance[next_node] = cost
                        heapq.heappush(q, (cost, next_node))
                    elif cost == distance[next_node]:
                        prev_node[next_node].append([cur_node,(next_node, c)])
        return distance


    result = dijkstra(s)
    queue = deque([d])
    visited = [False] * len(graph)
    while queue:
        node = queue.popleft()
        if visited[node]:
            continue
        visited[node] = True
        for info in prev_node[node]:
            p_node, road_info = info
            queue.append(p_node)
            if road_info in graph[p_node]:
                graph[p_node].remove(road_info)
    result = dijkstra(s)
    if result[d] == int(1e10):
        result[d] = -1
    print(result[d])

    n, m = map(int, input().split())
