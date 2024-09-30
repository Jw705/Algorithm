def solution(storey):
    answer = 0
    while storey:
        tmp = storey%10
        if tmp < 5:
            answer += tmp
        elif tmp == 5:
            if storey % 100 >= 50 and storey >= 100:   
                answer += 5
                storey += 10
            else:
                answer += 5                
        else:
            answer += (10 - tmp)
            storey += 10
        storey //= 10
            
    return answer