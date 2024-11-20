def base10toN(number, N):
    if number == 0:
        return '0'
    
    result = ''
    while number > 0:
        result = str(number % N) + result
        number //= N
    return result
    

def solution(expressions):
    questions = []
    parsed_expressions = []
    base = [False] * 2 + [True] * 8
    
    for expression in expressions:
        A, operator, B, _ , C = expression.split()
                    
        max_num = max(max(A), max(B), max(C))
        if C == 'X':
            questions.append([A, operator, B])
            max_num = max(max(A), max(B))
        else:
            parsed_expressions.append([A, operator, B, C])
        
        for i in range(2, int(max_num) + 1):
            if base[i] == True:
                base[i] = False
    
    for A, operator, B, C in parsed_expressions:
        for i in range(2, 10):
            if base[i] == False:
                continue            
            new_A, new_B, new_C = int(A, i), int(B, i), int(C, i)
            #print(i, [A, operator, B, C], [new_A, operator, new_B, new_C])
            if operator == '+' and new_A + new_B != new_C:
                base[i] = False
            elif operator == '-' and new_A - new_B != new_C:
                base[i] = False
    
    pos_base = []
    for i in range(2, 10):
        if base[i] == True:
            pos_base.append(i)
    #print(pos_base)
    
    answer = []
    for A, operator, B in questions:
        if operator == '+':
            C = base10toN(int(A, pos_base[0]) + int(B, pos_base[0]), pos_base[0])
        else:
            C = base10toN(int(A, pos_base[0]) - int(B, pos_base[0]), pos_base[0])
            
        #print([A, operator, B, C])
        for i in pos_base:
            if operator == '+':
                tmp_C = base10toN(int(A, i) + int(B, i), i)
            else:
                tmp_C = base10toN(int(A, i) - int(B, i), i)
                
            if tmp_C != C:
                C = '?'
                break
        #print([A, operator, B, C])
        answer.append(f'{A} {operator} {B} = {C}')
        
    return answer