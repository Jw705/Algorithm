import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])


def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)

    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    # 우선순위 큐에 삽입하는 튜플은 (거리, 노드) → heapq라이브러리는 튜플 첫 원소 기준으로 최소힙 구성
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드의 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for node, time in graph[now]:
            cost = dist + time
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, (cost, node))

    return distance

sum_arr = dijkstra(x)

for i in range(1, n + 1):
    sum_arr[i] += dijkstra(i)[x]

print(max(sum_arr[1:]))