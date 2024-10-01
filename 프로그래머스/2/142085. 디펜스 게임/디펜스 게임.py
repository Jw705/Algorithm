from collections import deque
import heapq

def solution(n, k, enemy):
    answer = 0 
    
    queue = deque([(0,n,k)])  
    past_enemy = []
    
    while queue:
        round_num, n_num, k_num = queue.popleft()
        if round_num == len(enemy):
            answer = round_num
        elif n_num < enemy[round_num]:  
            heapq.heappush(past_enemy,-1*enemy[round_num])
            # 게임 종료
            answer = round_num           
            if k_num > 0:
                max_before = -1*heapq.heappop(past_enemy)
                result = n_num + max_before - enemy[round_num]
                if result >= 0:
                    queue.append((round_num + 1, result, k_num - 1))
        else:
            heapq.heappush(past_enemy,-1*enemy[round_num])
            queue.append((round_num + 1, n_num - enemy[round_num], k_num))
    
    return answer