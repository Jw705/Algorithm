from collections import deque

def bfs(maps, start, visited, target):
    directions = [[-1,0],[1,0],[0,-1],[0,1]]
    queue = deque([start])
    visited[start[0]][start[1]] = 0
    
    while queue:
        v = queue.popleft()
        if maps[v[0]][v[1]] == target:
            break
        for i in range(4):
            ny = v[0]+directions[i][0]
            nx = v[1]+directions[i][1]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if visited[ny][nx] == -1 and maps[ny][nx] != 'X':
                    queue.append([ny,nx])
                    visited[ny][nx] = visited[v[0]][v[1]]+1  

def solution(maps):
    answer = 0
    visited = [ [-1] * len(maps[0]) for _ in range(len(maps)) ]
    
    start=[0,0]
    lever=[0,0]  
    exit=[0,0]    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]=='S':
                start=[i,j]
            if maps[i][j]=='L':
                lever=[i,j]
            if maps[i][j]=='E':
                exit=[i,j]
                
    bfs(maps,start,visited, 'L')
    stol=visited[lever[0]][lever[1]]
    if stol==-1:
        return -1
    
    visited = [ [-1] * len(maps[0]) for _ in range(len(maps)) ]
    bfs(maps,lever,visited, 'E')
    ltoe=visited[exit[0]][exit[1]]
    if ltoe==-1:
        return -1
    
    answer = stol+ltoe
    return answer