def solution(a, b, n):
    answer = 0
    while n>=a:
        new = (n//a)*b
        answer+=new
        n = new+(n%a)
    return answer