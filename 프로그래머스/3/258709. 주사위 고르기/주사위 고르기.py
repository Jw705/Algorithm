from itertools import combinations
from itertools import product
from bisect import bisect_left


def solution(dice):
    answer = []    
    dice_cnt = len(dice)
    
    주사위선택결과 = list(combinations(range(dice_cnt),dice_cnt//2))
    주사위굴린결과 = list(product(range(6), repeat=dice_cnt//2))
    
    배열 = []
    
    for i_dice in 주사위선택결과:
        I = []
        for 결과 in 주사위굴린결과:
            a_result = 1
            for i in range(dice_cnt//2):
                a_result += dice[i_dice[i]][결과[i]]
            I.append(a_result)
        I.sort()
        배열.append(I)
    
    max_win_count = 0
    win_count = [-1 for _ in range(len(주사위선택결과))]
    
    for k in range(len(주사위선택결과)):  
        if win_count[k] != -1:
            continue
        
        a_dice = 주사위선택결과[k]
        b_dice = []
        주사위배열 = list(주사위선택결과[k])
        for i in range(dice_cnt):
            if i not in a_dice:
                주사위배열.append(i)  
                b_dice.append(i)
        b_dice = tuple(b_dice)
        
        a_index = 주사위선택결과.index(a_dice)
        b_index = 주사위선택결과.index(b_dice)
        a_wins = sum(bisect_left(배열[b_index], num) for num in 배열[a_index])
        b_wins = sum(bisect_left(배열[a_index], num) for num in 배열[b_index])
        
        win_count[a_index] = a_wins
        win_count[b_index] = b_wins
        
    for 주사위 in 주사위선택결과[win_count.index(max(win_count))]:
        answer.append(주사위+1)
    
    return answer