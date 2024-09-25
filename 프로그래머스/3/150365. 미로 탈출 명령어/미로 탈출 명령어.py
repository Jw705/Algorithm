from collections import deque

def reachable(nx, ny, r, c, remain):
    distance = abs(nx - r) + abs(ny - c)
    return distance <= remain and (remain - distance) % 2 == 0
    

def solution(n, m, startX, startY, r, c, k):
    answer = ''
    
    if not reachable(startX, startY, r, c, k):
        return "impossible"
    
    queue = [(startX,startY,'',k)]
    while queue:
        x, y, route, remain = queue.pop()

        if len(route) == k:
            if x == r and y == c:
                return route
                break
        else:
            dx = [1, 0, 0, -1]
            dy = [0, -1, 1, 0]
            char = ['d', 'l', 'r', 'u']
            for i in range(3,-1,-1):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 < nx <= n and 0 < ny <= m and reachable(nx, ny, r, c, remain-1):
                    queue.append([nx, ny, route + char[i], remain-1])
                        
    return "impossible"