def find_약수_cnt(num):
    cnt=0
    for i in range(1,num//2+1):
        if num%i==0:
            cnt+=1
    return cnt+1            

def solution(left, right):
    answer = 0
    for i in range(left, right+1):       
        cnt = find_약수_cnt(i)
        if cnt%2==0:
            answer+=i
        else:
            answer-=i
    return answer