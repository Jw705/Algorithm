def solution(numbers):
    answer = 0
    arr=[False]*10
    for number in numbers:
        arr[number]=True
    for i in range(10):
        if arr[i]==False:
            answer+=i
    return answer