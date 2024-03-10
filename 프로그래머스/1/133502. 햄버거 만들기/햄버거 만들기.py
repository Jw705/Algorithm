def solution(ingredient):
    answer = 0
    stack=[]
    for i in ingredient:
        stack.append(i)
        if i==1 and len(stack) >= 4:
            if stack[-1] == 1 and stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                answer+=1
            
    return answer