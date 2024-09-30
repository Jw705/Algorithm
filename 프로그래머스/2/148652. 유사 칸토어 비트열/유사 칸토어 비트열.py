def find_zero(length, s, l, r):
    result = 0
    if s + length <= l:
        return 0
    elif r < s:
        return 0
    
    if length == 5:
        arr = [1,1,0,1,1]
        if s < l <= r <= s + 5:
            result = (arr[l-s:r-s+1].count(1))            
        elif s < l <= s + 4:
            result = (arr[l-s:].count(1))
        elif s <= r < s + 4:
            result = (arr[:r-s+1].count(1))
        else:
            result = 4
    else:
        tmp = length // 5        
        tmp_sum = 0
        for i in range(5):
            start = s + tmp * i                  
            if i == 2:
                tmp_sum += 0
            else:
                tmp_sum += find_zero(tmp, start, l, r)
        result += tmp_sum
    return result
    
    
def solution(n, l, r):
    answer = find_zero(5**n, 1, l, r)
    return answer