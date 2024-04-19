def solution(numbers):
    pos_arr = [0]*201
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            pos_arr[numbers[i]+numbers[j]]=1
    
    answer = []
    for i in range(len(pos_arr)):    
        if pos_arr[i]==1:
            answer.append(i)
            
    return answer