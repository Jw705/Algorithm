from collections import deque

def bfs(graph, startX, startY):
    visited = [[False for _ in range(5)] for _ in range(5)]
    queue = deque([[0, startX, startY]])
    visited[startX][startY] = True
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    while queue:
        distance, x, y = queue.popleft()
        if distance == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue            
            if not visited[nx][ny] and graph[nx][ny] == 'P':
                return False                        
            if not visited[nx][ny] and graph[nx][ny] == 'O':
                visited[nx][ny] = True
                queue.append([distance + 1, nx, ny])
    return True

def solution(places):
    answer = []
    for place in places:
        is_safe = 1
        
        P_list = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    P_list.append([i, j])
                    
        for i, j in P_list:
            if bfs(place, i, j) == False:
                is_safe = 0
                break
        answer.append(is_safe)
        
    return answer