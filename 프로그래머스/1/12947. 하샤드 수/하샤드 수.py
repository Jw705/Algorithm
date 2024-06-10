def solution(x):
    answer = False
    tmp=x
    sum=0
    while(tmp>0):        
        sum+=tmp%10
        tmp//=10
    if x % sum == 0:
        answer=True    
    return answer