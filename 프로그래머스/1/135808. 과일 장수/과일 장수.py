import heapq

def solution(k, m, score):    
    score.sort()
    box=[]
    answer = 0
    for i in range(len(score)%m,len(score)):
        box.append(score[i])
        if len(box)==m:
            answer+=box[0]*m
            box=[]
    return answer