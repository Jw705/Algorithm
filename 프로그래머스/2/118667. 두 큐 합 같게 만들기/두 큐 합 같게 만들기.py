def solution(queue1, queue2):
    sum_a = sum(queue1)
    sum_b = sum(queue2)
    if sum_a == sum_b:
        return 0
    if (sum_a + sum_b) % 2 == 1:
        return -1
    
    target = (sum_a + sum_b) // 2
    queue = queue1 + queue2
    n = len(queue)
    
    # 투 포인터 알고리즘으로 합이 target이 되는 범위 찾기
    a = 0
    b = 1
    tmp_sum = queue[0]    
    answer = int(1e9)
    
    while a <= b and b < n:
        if tmp_sum == target:
            task_cnt = 0
            
            if a >= (n // 2):
                task_cnt = (b - n // 2) + a
            elif b > (n // 2):
                task_cnt = (b - n // 2) + a
            elif b == n // 2:
                task_cnt = a
            else:
                task_cnt = (b + n // 2) + a
                
            answer = min(task_cnt, answer)
        
        if tmp_sum >= target:
            tmp_sum -= queue[a]
            a += 1
        elif tmp_sum < target:
            tmp_sum += queue[b]
            b += 1
    
    if answer == int(1e9):
        answer = -1
        
    return answer