def solution(food):
    answer = ''
    for i in range(1, len(food)):
        print(food[i])
        for _ in range(food[i]//2):
            answer+=(str(i))
    answer += '0' + answer[::-1]
    return answer