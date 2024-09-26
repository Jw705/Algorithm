import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [-1 for _ in range(n + 1)]
parent[1] = 0

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


stack = []
stack.append(1)
while stack:
    current_node = stack.pop()
    for node in graph[current_node]:
        if parent[node] == -1:
            parent[node] = current_node
            stack.append(node)

for i in range(2, n + 1):
    print(parent[i])
