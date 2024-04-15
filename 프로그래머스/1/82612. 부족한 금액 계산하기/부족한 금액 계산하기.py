def solution(price, money, count):    
    answer = 0
    for i in range(count):
        answer += price*(i+1)
    answer -= money
    if answer<0:
        return 0
    return answer