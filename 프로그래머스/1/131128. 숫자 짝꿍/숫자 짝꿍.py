def solution(X, Y):
    answer = ''
    cnt_x=[0,0,0,0,0,0,0,0,0,0]
    cnt_y=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(X)):
        cnt_x[int(X[i])]+=1
    for i in range(len(Y)):
        cnt_y[int(Y[i])]+=1
    ans=0
    for i in range(9, -1, -1):
        if cnt_x[i]>0 and cnt_y[i]>0:
            for _ in range(min(cnt_x[i],cnt_y[i])):
                ans*=10
                answer+=str(i)
    if answer=="":
        return "-1"
    if answer[0]=="0":
        return "0"        
    return answer