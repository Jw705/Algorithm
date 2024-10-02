import sys
import heapq

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, d, c = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])

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
                        distance[next_node] = cost
                        heapq.heappush(q, (cost, next_node))
        return distance

    result = dijkstra(c)
    infection_cnt = 0
    infection_time = 0
    for i in range(1, n+1):
        if result[i] != int(1e10):
            infection_cnt += 1
            infection_time = max(infection_time, result[i])

    print(infection_cnt, infection_time)