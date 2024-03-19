import math

def solution(weights):
    answer = 0
    arr = [0]*2001
    
    for weight in weights:  
        arr[weight]+=1
        
    for weight in weights:
        if arr[weight]>1:
            answer+=math.comb(arr[weight], 2) / arr[weight]
        if arr[weight*2]>0:
            answer+=arr[weight*2]
        if (weight*(3/2)==int(weight*(3/2))) and arr[int(weight*(3/2))]>0:
            answer+=arr[int(weight*(3/2))]
        if (weight*(4/3)==int(weight*(4/3))) and arr[int(weight*(4/3))]>0:
            answer+=arr[int(weight*(4/3))]
    return answer