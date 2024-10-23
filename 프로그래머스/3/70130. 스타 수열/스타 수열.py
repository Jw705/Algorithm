def solution(a):
    
    num_dict = dict()  
    
    for i in range(len(a)):
        if not a[i] in num_dict:
            num_dict[a[i]] = [0,-1]
            
        if i > 0 and num_dict[a[i]][1] < i - 1 and a[i - 1] != a[i]:
            num_dict[a[i]][0] += 2
            num_dict[a[i]][1] = i
        elif i < len(a) - 1 and num_dict[a[i]][1] < i and a[i + 1] != a[i]:
            num_dict[a[i]][0] += 2
            num_dict[a[i]][1] = i + 1
    
    answer = 0
    for max_star_sequence_length, a in num_dict.values():
        answer = max(answer, max_star_sequence_length)
    
    return answer