from collections import deque

def solution(stones, k):
    answer = 200000001
    queue = deque()  # 현재 윈도우에서 유효한 값들의 인덱스를 저장할 deque
    
    for i in range(len(stones)):
        # 현재 인덱스가 k를 넘어가면 윈도우 밖의 값을 deque에서 제거
        if queue and queue[0] < i - k + 1:
            queue.popleft()
        
        # 현재 값이 deque에 있는 값들보다 크면 필요 없는 값들을 제거
        while queue and stones[queue[-1]] <= stones[i]:
            queue.pop()
        
        # 현재 인덱스를 deque에 추가
        queue.append(i)
        
        # 윈도우가 k 크기에 도달하면 최댓값 갱신
        if i >= k - 1:
            answer = min(answer, stones[queue[0]])
    
    return answer