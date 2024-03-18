def solution(numbers):
    answer = [-1]*len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while len(stack)>0:
            if stack[-1][0]<numbers[i]:
                num,idx = stack.pop()
                answer[idx] = numbers[i]
            else:
                break        
        stack.append([numbers[i],i])
    return answer