import sys
sys.setrecursionlimit(5000)

def solution(maps):
    answer = []
    visited=[ [0 for _ in range(len(maps[0]))] for _ in range(len(maps)) ]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j]=True
                answer.append(dfs(maps,[i,j],visited))
                
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer

def dfs(maps, v, visited):
    x,y = v
    area = int(maps[x][y])
    
    direction = [[-1,0],[1,0],[0,-1],[0,1]]
    for direct in direction:
        dx,dy = direct
        nx = x+dx
        ny = y+dy
        
        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
            if maps[nx][ny] != 'X' and not visited[nx][ny] :
                visited[nx][ny] = True
                area += dfs(maps, [nx,ny], visited)
            
    return area