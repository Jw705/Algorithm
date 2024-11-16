def solution(h1, m1, s1, h2, m2, s2):
    start = h1 * 60 * 60 + m1 * 60 + s1
    end = h2 * 60 * 60 + m2 * 60 + s2
       
    answer = 0 
    if start == 0 or start == 12 * 60 * 60:
        answer += 1
    
    for i in range(start, end):
        h = (i / 120) % 360
        m = (i / 10) % 360
        s = (i * 6) % 360
        
        nh = ((i + 1) / 120) % 360
        nm = ((i + 1) / 10) % 360
        ns = ((i + 1) * 6) % 360
        
        if nh == 0:
            nh = 360
        if nm == 0:
            nm = 360
        if ns == 0:
            ns = 360
        
        if nh == nm == ns:
            answer += 1
        else:
            if s < h and ns >=nh:
                answer += 1
            if s < m and ns >= nm:
                answer += 1
        
    
           
    return answer