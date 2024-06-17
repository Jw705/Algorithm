import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = 1

    # 외부노드(leaf)이면 부모를 early adaptor로 설정
    if len(graph[v]) == 1 and visited[graph[v][0]] != 0:
        visited[v] = 2 # 완전히 탐색이 끝났다는 의미로 2로 표시
        visited[graph[v][0]] = 'early adaptor'
        
    else:
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if visited[i] == 0:
                dfs(graph, i, visited)

        # 자식 노드 순회를 끝낸 후, 본인이 early adaptor가 아닐 때
        if visited[v] != 'early adaptor':
            # early adaptor가 아닌 자식이 있으면 본인이 early adaptor가 된다.
            for j in graph[v]:
                if visited[j] == 2:
                    visited[v] = 'early adaptor'
                    return
            visited[v] = 2


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited)

res = 0
for i in range(n + 1):
    if visited[i] == 'early adaptor':
        res += 1

print(res)