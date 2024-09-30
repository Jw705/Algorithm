def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:x[0],reverse=True)
    data.sort(key=lambda x:x[col-1])
    S=[]
    for i in range(row_begin, row_end+1):
        S_i = 0
        for d in data[i-1]:
            S_i += d % i
        S.append(S_i)
    answer = S[0]
    for i in range(1,len(S)):
        answer = answer^S[i]
    return answer