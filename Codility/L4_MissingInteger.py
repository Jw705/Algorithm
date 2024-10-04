def solution(A):
    is_include = [False] * 1000001
    for num in A:
        if num > 0:
            is_include[num] = True
    
    for i in range(1,1000001):
        if not is_include[i]:
            return i