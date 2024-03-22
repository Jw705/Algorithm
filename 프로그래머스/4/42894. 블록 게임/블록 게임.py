def is_not_zero_upper(board,i,j):
    while(i>0):
        i-=1
        if board[i][j]!=0:
            return False
    return True

def find_pos_black_block(board,i,j):
    block_num = board[i][j]
    
    pos_b1 = i+1<len(board) and j-2>=0 and board[i+1][j-2]==block_num and is_not_zero_upper(board,i+1,j-2)
    pos_b2 = i+1<len(board) and j-1>=0 and board[i+1][j-1]==block_num and is_not_zero_upper(board,i+1,j-1)
    pos_b3 = i+1<len(board) and board[i+1][j]==block_num
    pos_b4 = i+1<len(board) and j+1<len(board[0]) and board[i+1][j+1]==block_num and is_not_zero_upper(board,i+1,j+1)
    pos_b5 = i+1<len(board) and j+2<len(board[0]) and board[i+1][j+2]==block_num and is_not_zero_upper(board,i+1,j+2)
    
    pos_b6 = i+2<len(board) and j-1>=0 and board[i+2][j-1]==block_num and is_not_zero_upper(board,i+2,j-1)
    pos_b7 = i+2<len(board) and board[i+2][j]==block_num
    pos_b8 = i+2<len(board) and j+1<len(board[0]) and board[i+2][j+1]==block_num and is_not_zero_upper(board,i+2,j+1)
    
    
    if (pos_b1 and pos_b2 and pos_b3):
        board[i][j] = 0
        board[i+1][j-2] = 0
        board[i+1][j-1] = 0
        board[i+1][j] = 0
        return 1        
    elif (pos_b2 and pos_b3 and pos_b4):
        board[i][j] = 0
        board[i+1][j-1] = 0
        board[i+1][j] = 0
        board[i+1][j+1] = 0
        return 1    
    elif (pos_b3 and pos_b4 and pos_b5):
        board[i][j] = 0
        board[i+1][j] = 0
        board[i+1][j+1] = 0
        board[i+1][j+2] = 0
        return 1    
    elif (pos_b3 and pos_b6 and pos_b7):
        board[i][j] = 0
        board[i+1][j] = 0
        board[i+2][j] = 0
        board[i+2][j-1] = 0
        return 1
    elif (pos_b3 and pos_b7 and pos_b8):
        board[i][j] = 0
        board[i+1][j] = 0
        board[i+2][j] = 0
        board[i+2][j+1] = 0
        return 1
    else:
        return 0
    
'''
가능한 블록
  0  0  0
000 000 000

 0 0
 0 0
00 00

  0
12345
 678
'''    

def solution(board):
    answer = 0
    tmp_answer = 1
    
    while tmp_answer > 0:
        tmp_answer = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]>0:
                    tmp_answer += find_pos_black_block(board,i,j)
        answer += tmp_answer
          
    return answer
