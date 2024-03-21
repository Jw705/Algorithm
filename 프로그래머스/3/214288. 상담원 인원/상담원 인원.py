from itertools import product

def solution(k, n, reqs):          
    arr = [[] for _ in range(k+1)]
    for req in reqs:
        a,b,c=req
        arr[c].append([a,b])
    
    waiting_time = [[0 for _ in range(n-k+1) ] for _ in range(k+1)]   
    
    # 멘토 수 별 대기시간 계산         
    for i in range(1,k+1):
        for j in range(n-k+1):
            time=[0]*(j+1)
            
            for r in arr[i]:
                a, b = r
                time.sort()
                
                is_resv = False
                for l in range(j+1):
                    if time[l] <= a:
                        time[l] = a+b
                        is_resv = True
                        break
                if is_resv == False:
                    waiting_time[i][j]+=time[0]-a
                    time[0]=time[0]+b              

    
    answer = int(1e9)
    # 멘토 배치 경우의 수를 모두 찾아 최소 대기시간 갱신
    for p in product(range(1,n+1),repeat=k):
        if sum(p) == n:
            tmp = 0
            for i in range(1,k+1):
                tmp+=(waiting_time[i][p[i-1]-1])
            answer = min(answer,tmp)

    return answer