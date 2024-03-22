from itertools import product, combinations

def solution(orders, course):
    orders.sort(key = lambda x:len(x))
        
    answer = []    
    test = []
    pos_course = dict()
    for order in orders:
        for i in course:
            for p in list(combinations(order,i)):
                a = ''.join(sorted(list(p)))
                if a in pos_course:
                    pos_course[a]+=1
                else:
                    pos_course[a]=1
    
    max_course = [[['',0]] for _ in range(11)]  
    
    for i in course:                                           
        for key, value in pos_course.items():
            if len(key)==i and value>max_course[i][0][1]:
                max_course[i]=[[key, value]]
            elif len(key)==i and value==max_course[i][0][1]:
                max_course[i].append([key, value])
            
    for i in course: 
        for c in max_course[i]:
            if c[1]>=2:
                answer.append(c[0])
            
    return sorted(answer)


