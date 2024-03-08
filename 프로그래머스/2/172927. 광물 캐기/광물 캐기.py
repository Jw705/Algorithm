# 24.03.08 28m

def solution(picks, minerals):
    answer = 0
    피로도 = [[1,1,1],[5,1,1],[25,5,1]]
    
    costs=[]
    for i in range(0,sum(picks)*5,5):
        cost = [0,0,0]
        for j in range(i,i+5):
            if j<len(minerals):
                if (minerals[j] == 'diamond'):
                    cost[0]+=피로도[0][0]
                    cost[1]+=피로도[1][0]
                    cost[2]+=피로도[2][0]
                elif (minerals[j] == 'iron'):
                    cost[0]+=피로도[0][1]
                    cost[1]+=피로도[1][1]
                    cost[2]+=피로도[2][1]
                elif (minerals[j] == 'stone'):
                    cost[0]+=피로도[0][2]
                    cost[1]+=피로도[1][2]
                    cost[2]+=피로도[2][2]
        costs.append(cost)
        
    costs.sort(key = lambda x : x[2], reverse=True)
        
    for cost in costs:
        if picks[0] > 0:
            answer+=cost[0]
            picks[0]-=1
        elif picks[1] > 0:
            answer+=cost[1]
            picks[1]-=1
        elif picks[2] > 0:
            answer+=cost[2]
            picks[2]-=1            
    
    return answer