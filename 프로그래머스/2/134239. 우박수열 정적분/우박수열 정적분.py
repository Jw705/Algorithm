def solution(k, ranges):
    ubak = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
            ubak.append(k)
        else:
            k = k * 3 + 1
            ubak.append(k)
    
    integral = []
    for i in range(len(ubak)-1):
        area = min(ubak[i], ubak[i + 1]) + abs(ubak[i]-ubak[i+1]) / 2.0
        integral.append(area)
    
    answer = []
    for r in ranges:
        a = r[0]
        b = len(ubak) + r[1] - 1
        if a > b:
            answer.append(-1.0)
        else:
            answer.append(sum(integral[a:b]))
        
    return answer