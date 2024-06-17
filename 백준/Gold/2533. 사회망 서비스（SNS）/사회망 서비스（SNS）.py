import sys

sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline


def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = 1

    # 외부노드(leaf)이면 부모를 early adaptor로 설정
    if len(graph[v]) == 1 and visited[graph[v][0]] != 0:
        visited[v] = 2
        visited[graph[v][0]] = 'early adaptor'
        #print(v, '의 부모', graph[v][0], '는 얼리어답터')

    else:
        # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
        for i in graph[v]:
            if visited[i] == 0:
                dfs(graph, i, visited)

        # 자식 노드 순회를 끝낸 후, 본인이 early adaptor가 아니면
        if visited[v] != 'early adaptor':
            #print(v, '자식 탐색 시작')
            # 자식 노드가 하나라도 Early Adopter가 아니면 본인이 Early Adopter가 된다.
            for j in graph[v]:
                if visited[j] == 2:
                    visited[v] = 'early adaptor'
                    #print(v, '의 자식', j, '가 얼리어답터가 아니므로 얼리로')
                    return
            visited[v] = 2
            '''
            # 본인 부모를 early adaptor로 설정
            visited[v] = 2
            if len(graph[v]) > 0:
                visited[graph[v][0]] = 'early adaptor'
            '''


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(graph, 1, visited)

#print(visited)

res = 0
for i in range(n + 1):
    if visited[i] == 'early adaptor':
        res += 1

print(res)

'''
8
1 2
1 3
1 4
2 5
2 6
4 7
4 8

4
1 2
2 3
3 4

4
1 2
3 4
2 4
'''
