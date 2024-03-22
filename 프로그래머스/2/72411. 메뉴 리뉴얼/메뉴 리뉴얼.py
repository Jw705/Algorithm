from itertools import combinations

def solution(orders, course):
    answer = []    
    
    # 만들 수 있는 모든 코스를 키로, 등장 횟수를 value로 저장
    pos_course = dict()
    
    # 모든 order를 보면서 pos_course의 값을 갱신
    for order in orders:
        for i in course:
            # order에서 가능한 코스는 조합(combinations)을 이용하여 찾기
            for comb in list(combinations(order,i)):
                # 코스 이름은 알파벳순서로 정렬된 문자열로 만들기
                course_name = ''.join(sorted(list(comb)))
                if course_name in pos_course:
                    pos_course[course_name]+=1
                else:
                    pos_course[course_name]=1
    
    # 가능한 코스별 단품 개수별로 가장 많이 등장하는 코스르 저장할 배열
    max_course = [[['',0]] for _ in range(11)]  
    
    # 단품 개수별로 가장 많이 등장하는 코스를 max_course에 저장
    for i in course:                                           
        for key, value in pos_course.items():
            if len(key)==i and value>max_course[i][0][1]:
                max_course[i]=[[key, value]]
            elif len(key)==i and value==max_course[i][0][1]:
                max_course[i].append([key, value])
    
    # 최소 2명 이상의 손님으로부터 주문된 코스만 정답에 추가
    for i in course: 
        for c in max_course[i]:
            if c[1]>=2:
                answer.append(c[0])
    
    # 알파벳 순서로 정렬하여 반환
    return sorted(answer)


