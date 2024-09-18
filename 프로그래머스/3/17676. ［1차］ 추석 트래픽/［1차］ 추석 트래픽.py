def solution(lines):
    answer = 0
    new_lines = []
    tmp_arr = []
    
    for line in lines:
        # 입력 데이터 전처리
        S1, S2, T = line.split()
        T = int(float(T[0:-1])*1000) - 1
        S3 = S2.split(":")
        
        end_time = int(S3[0])*60*60*1000 + int(S3[1])*60*1000 + int(float(S3[2])*1000)
        start_time = end_time - T
        
        new_lines.append([start_time, end_time])
        tmp_arr.append(start_time)
        tmp_arr.append(end_time)
        
    new_lines.sort()    
    tmp_arr.sort()
    
    for time in tmp_arr:
        a = time
        b = a+999
        cnt = 0
        for j in range(len(new_lines)):
            s,e = new_lines[j]
            if a<=s<=b or a<=e<=b or(s<=a and b<=e):
                cnt+=1
        answer = max(cnt,answer)
                
        
        
    return answer