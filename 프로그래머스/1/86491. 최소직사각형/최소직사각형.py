def solution(sizes):
    
    tmp=[0,0]
    for size in sizes:
        w, h = size
        if w<h:
            tmp[0]=max(tmp[0],h)
            tmp[1]=max(tmp[1],w)
        else:
            tmp[0]=max(tmp[0],w)
            tmp[1]=max(tmp[1],h)
            
    answer = tmp[0]*tmp[1]
    return answer