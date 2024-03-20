from collections import deque

def has_zero_around(arr, y, x):
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if arr[y + dy][x + dx] == 0:
                return True
    return False

def bfs(graph,start,target,visited):    
    sx,sy = start
    queue = deque([(sx,sy,0)])    
    visited[sx][sy]=1
    
    directions=[[1,0],[-1,0],[0,-1],[0,1]]    
    while queue:
        x, y, l = queue.popleft()
        if [x,y] == target:
            return l/2
        for direction in directions:
            dx, dy = direction
            nx = x+dx
            ny = y+dy
            
            조건1 = 0<nx<101 and 0<ny<101
            조건2 = (visited[nx][ny] == 0)
            조건3 = (graph[nx][ny] == 1)
            if 조건1 and 조건2 and 조건3:   
                queue.append([nx,ny,l+1])
                visited[nx][ny] = 1

def solution(rectangle, characterX, characterY, itemX, itemY):
    fill=[[0 for _ in range(105)]for _ in range(105)]
    graph=[[0 for _ in range(105)]for _ in range(105)]
    visited=[[0 for _ in range(105)]for _ in range(105)]
    
    for rect in rectangle:
        sx,sy,ex,ey=rect
        for x in range(sx*2,ex*2+1):
            for y in range(sy*2,ey*2+1):
                fill[x][y]=1   
        
    for y in range(0,101):
        for x in range(0,101):
            if fill[x][y] == 1 and has_zero_around(fill, x, y):
                graph[x][y]=1
                
    answer = bfs(graph,[characterX*2, characterY*2], [itemX*2, itemY*2],visited)
    
    return answer