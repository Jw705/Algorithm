def solution(scores):
    rank_sum = []
    원호_a = scores[0][0]
    원호_b = scores[0][1]
    
    min_score = [-1 for _ in range(100002)]
    
    for a, b in scores:
        min_score[a] = max(min_score[a], b)
    
    cur_max_b = -1
    for i in range(100001, -1, -1):
        min_score[i] = max(cur_max_b, min_score[i])
        cur_max_b = max(cur_max_b, min_score[i])
    
    if min_score[원호_a + 1] > 원호_b:
        return -1 
    for a, b in scores:
        if min_score[a + 1] <= b:
            rank_sum.append(a + b)
    
    answer = 0
    rank_sum.sort(reverse = True)
    for i in range(len(rank_sum)):
        if rank_sum[i] == 원호_a + 원호_b:
            answer = i + 1
            break
    
    return answer