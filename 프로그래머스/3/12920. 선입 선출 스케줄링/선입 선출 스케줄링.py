def find_finished_task(time, cores):
    finished_task = len(cores)
    for core in cores:
        finished_task += (time // core)
    return finished_task
    

def solution(n, cores):
    answer = 0
    time = -1
    
    l = 0
    r = 50000 * 10000
    while l < r:        
        mid = (l + r) // 2
        finished_task = find_finished_task(mid, cores)
        #print([l,r], mid, finished_task)
        if finished_task >= n:
            time = mid
            r = mid
        else:
            l = mid + 1
            
    
    left_task = n - find_finished_task(time - 1, cores)  
    for i in range(len(cores)):
        if time % cores[i] == 0:  
            left_task -= 1
        if left_task == 0:
            answer = (i + 1)
            break
    
       
    return answer