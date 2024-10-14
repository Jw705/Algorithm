# 60m
import math
from collections import deque

def update_route(graph, route, node):
    cur_next_node = route[node]
    if cur_next_node == -1:
         route[node] = route[node]
    elif cur_next_node == len(graph[node]) - 1:
        route[node] = 0
    else:
        route[node] = route[node] + 1
    

def drop_number(graph, route):
    queue = deque([1])
    update_route(graph, route, 0)    
    while queue:
        cur_node = queue.popleft()                
        if route[cur_node] == -1: # 리프 노드 도착
            return cur_node
        else:
            next_node = graph[cur_node][route[cur_node]]
            update_route(graph, route, cur_node)
            queue.append(next_node)   
    

def solution(edges, target):
    node_cnt = len(edges) + 2
    graph = [[] for _ in range(node_cnt)]
    answer = []
    
    for parent_node, child_node in edges:
        graph[parent_node].append(child_node)
    
    # 초기 route 설정
    route = [-1 for _ in range(node_cnt)]
    for i in range(node_cnt):
        if len(graph[i]) > 0:
            graph[i].sort()
            route[i] = 0
            
    max_target_value = max(target)
    max_drop_cnt = (max_target_value + 2) // 3
    
    drop_info = [[] for _ in range(len(target))]
    order = []
    max_target = max(target)
    
    j = 1
    is_final = False
    while True:
        cur_leaf_node = drop_number(graph, route) - 1
        
        isAvailableCardAmount = True
        for i in range(len(target)):
            cur_max_drop = target[i]
            cur_min_drop = math.ceil(target[i] / 3)
            if len(drop_info[i]) < cur_min_drop:
                isAvailableCardAmount = False
            if len(drop_info[i]) > cur_max_drop:
                return [-1]
            
        if (isAvailableCardAmount):
            break
        drop_info[cur_leaf_node].append(j)
        order.append(cur_leaf_node + 1)
        j += 1
        
    answer = [0] * len(order)
    
    for i in range(len(drop_info)):
        if len(drop_info[i]) > 0:
            for j in range(len(drop_info[i])-1,-1,-1):
                if j == 0:
                    if target[i] > 3 or target[i] < 1:
                        return [-1]
                    else:
                        drop_info[i][j] = (drop_info[i][j],target[i])
                        target[i] = 0
                else:
                    if (target[i] - 3) >= j:
                        drop_info[i][j] = (drop_info[i][j],3)
                        target[i] -= 3
                    elif (target[i] - 2) >= j:
                        drop_info[i][j] = (drop_info[i][j],2)
                        target[i] -= 2
                    elif (target[i] - 1) >= j:
                        drop_info[i][j] = (drop_info[i][j],1)
                        target[i] -= 1
                    else:
                        return [-1]                       
                               
                answer[drop_info[i][j][0] - 1] = drop_info[i][j][1]
    
            
    return answer