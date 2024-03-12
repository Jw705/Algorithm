def solution(board):
    answer = -1
    cnt=[0,0]
    result = ""    
        
    for i in range(3):            
        for j in range(3): 
            if board[i][j]=='O': 
                cnt[0]+=1
            elif board[i][j]=='X': 
                cnt[1]+=1
        
    for i in range(3):
        type1 = board[i][0]==board[i][1]==board[i][2]
        type2 = board[0][i]==board[1][i]==board[2][i]        
        
        if (type1 and board[i][0]=='O') or (type2 and board[0][i]=='O'):
            if result=="" or result=="O win":
                result="O win"
            else:
                return 0
        elif (type1 and board[i][0]=='X') or (type2 and board[0][i]=='X'):
            if result=="" or result=="X win":
                result="X win"
            else: 
                return 0  
            
    type3 = board[0][0]==board[1][1]==board[2][2]
    type4 = board[0][2]==board[1][1]==board[2][0]   
    if (type3 or type4) and board[1][1]=='O':
        if result=="" or result=="O win":
            result="O win"
        else:
            return 0
    elif (type3 or type4) and board[1][1]=='X':
        if result=="" or result=="X win":
            result="X win"
        else:
            return 0
    
    if cnt[0]-cnt[1]>1 or cnt[0]-cnt[1]<0:
        return 0
    elif cnt[0]==cnt[1]:
        if result=="O win":
            return 0
        else:
            return 1
    elif cnt[0]>cnt[1]:
        if result=="X win":
            return 0
        else:
            return 1
    else:   
        return 1
        
    
    
    return answer