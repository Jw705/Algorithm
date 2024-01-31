import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

for i in range(0, m):
    a, b = list(map(int, sys.stdin.readline().split()))
    graph[a].append([b, 1])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(x)
cnt = 0
for i in range(len(distance)):
    if distance[i] == k:
        cnt += 1
        print(i)

if cnt == 0:
    print(-1)

'''
4 4 2 1
1 2
1 3
2 3
2 4
'''
