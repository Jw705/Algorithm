# 7m

def solution(survey, choices):
    score = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    n = len(survey)
    for i in range(n):
        if choices[i] >= 5:
            score[survey[i][1]] += (choices[i] - 4)
        elif choices[i] <= 3:
            score[survey[i][0]] += (4 - choices[i])
    
    answer = ''
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
        
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
        
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'
        
    return answer