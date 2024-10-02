import sys
import heapq
from collections import deque

input = sys.stdin.readline


def dijkstra(start, n, graph):
    distance = [int(1e10)] * n
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    prev_node = [[] for _ in range(n)]

    while q:
        dist, cur_node = heapq.heappop(q)
        if distance[cur_node] < dist:
            continue
        for next_node, c in graph[cur_node]:
            cost = dist + c
            if cost < distance[next_node]:
                distance[next_node] = cost
                prev_node[next_node] = [cur_node]
                heapq.heappush(q, (cost, next_node))
            elif cost == distance[next_node]:
                prev_node[next_node].append(cur_node)

    return distance, prev_node


def remove_shortest_path(prev_node, graph, dest):
    q = deque([dest])
    visited = [False] * len(graph)
    while q:
        node = q.popleft()
        if visited[node]:
            continue
        visited[node] = True
        for prev in prev_node[node]:
            graph[prev] = [(v, w) for v, w in graph[prev] if v != node]
            q.append(prev)


# 입력 처리
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    s, d = map(int, input().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, input().split())
        graph[u].append((v, p))

    # 1. 다익스트라로 최단 경로와 이전 노드 정보 얻기
    distance, prev_node = dijkstra(s, n, graph)

    # 2. 최단 경로가 존재하면, 그 경로를 그래프에서 제거
    if distance[d] != int(1e10):
        remove_shortest_path(prev_node, graph, d)

    # 3. 간선이 제거된 그래프에서 다시 다익스트라 실행
    new_distance, _ = dijkstra(s, n, graph)

    # 4. 도착점 d에 도달할 수 없으면 -1 출력
    if new_distance[d] == int(1e10):
        print(-1)
    else:
        print(new_distance[d])
