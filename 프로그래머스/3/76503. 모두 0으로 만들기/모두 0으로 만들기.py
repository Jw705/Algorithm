from collections import deque

def solution(a, edges):
    n = len(a)
    tree = [set() for _ in range(n)]
    for u, v in edges:
        tree[u].add(v)
        tree[v].add(u)
    
    queue = deque([])
    for i in range(n):
        if len(tree[i]) == 1:
            queue.append(i)
    
    
    answer = 0
    while queue:
        i = queue.popleft()
        if tree[i]:
            node = sorted(tree[i])[0]  # tree[i]는 비어 있지 않다고 가정
        else:
            if a[i] != 0:
                answer = -1
            continue
        
        answer += abs(a[i])
        a[node] += a[i]
        a[i] = 0
        
        tree[i].remove(node)
        tree[node].remove(i)
        if len(tree[node]) == 1:
            queue.append(node)
        
        
    return answer