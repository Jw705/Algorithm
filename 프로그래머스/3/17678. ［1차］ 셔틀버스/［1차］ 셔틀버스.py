from collections import deque

def is_last_time(parsed_timetable, target, n, m, t):
    new_table = []
    for i in parsed_timetable:
        new_table.append(i)
    
    new_table.append(target)
    queue = deque(sorted(new_table))
    
    cur_time = 9 * 60    
    last_time = -1
    while cur_time < 24 * 60 and n > 0 and len(queue) > 0:
        for _ in range(m):
            if queue[0] <= cur_time:
                last_time = queue.popleft()
            if len(queue) == 0:
                break        
        cur_time += t
        n -= 1
        
    #print('결과 :', queue)
    #print('결과 :', [last_time,target], f'{last_time // 60}:{last_time % 60}', queue, n, m)
    if len(queue) == 0 or target < queue[0]:
        return True
    else:
        return False
    

def solution(n, t, m, timetable):
    answer = ''
    parsed_timetable = []
    for time in timetable:
        hh, mm = map(int, time.split(":"))
        parsed_timetable.append(hh * 60 + mm)
    
    answer_time = 24 * 60
    l = 0
    r = 24 * 60 - 1
    while l <= r:
        mid = (l + r) // 2
        #print(mid, f'{mid // 60}:{mid % 60}', end = ' ')
        if is_last_time(parsed_timetable, mid, n, m, t):
            #print('true')
            answer_time = mid
            l = mid + 1
        else:
            #print('false')
            r = mid - 1
        
    #print('정답', answer_time, f'{answer_time // 60}:{answer_time % 60}')
    hh = answer_time // 60
    mm = answer_time % 60
    if hh < 10:
        answer = '0' + str(hh)
    else:        
        answer = str(hh)
    if mm < 10:
        answer = answer + ':0' + str(mm)
    else:        
        answer = answer + ':' + str(mm)
    
    #last_time = find_last_time(parsed_timetable, n, m, t)
    #print(f'{last_time // 60}:{last_time % 60}', n, m)
        
    return answer