import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())

graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    graph[parent].append([child, weight])
    graph[child].append([parent, weight])

result = 0


def dfs(v, h):
    visited[v] = True

    child_height = [0, 0]
    for node, weight in graph[v]:
        if not visited[node]:
            child_height.append(dfs(node, h + weight) + weight)

    child_height.sort(reverse=True)
    global result
    result = max(result, child_height[0] + child_height[1])

    return child_height[0]

dfs(1, 0)
print(result)