from itertools import permutations

def solution(babbling):
    answer = 0
    possible_word = ["aya", "ye", "woo", "ma"]
    
    for word in babbling:
        prev_word = ""
        tmp=""
        for w in word:
            tmp+=w
            if tmp in possible_word and tmp!=prev_word:
                prev_word = tmp
                tmp=""
        if tmp=="":
            answer+=1                
        
    return answer