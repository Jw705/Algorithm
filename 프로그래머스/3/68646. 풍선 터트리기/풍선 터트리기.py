def solution(a):
    answer = 0
    min_start_left = [0] * len(a)
    min_start_right = [0] * len(a)
    min_start_left[0] = a[0]
    min_start_right[len(a) - 1] = a[len(a) - 1]
    for i in range(1, len(a)):
        min_start_left[i] = min(a[i], min_start_left[i - 1])
    for i in range(len(a)-2, -1, -1):
        min_start_right[i] = min(a[i], min_start_right[i + 1])
    
    for i in range(len(a)):
        small_num_cnt = 0
        if min_start_left[i] < a[i]:
            small_num_cnt += 1
        if min_start_right[i] < a[i]:
            small_num_cnt += 1
        #print([min_start_left[i], a[i], min_start_right[i]], small_num_cnt)
        if small_num_cnt < 2:
            answer += 1
    
    #print(min_start_left)
    #print(min_start_right)
    return answer