def solution(coin, cards):
    n = len(cards)
    cur_idx = n // 3
    origin_cards = dict()
    new_cards = dict()
    
    for i in range(cur_idx):
        origin_cards[cards[i]] = True
    
    answer = 0
    while True:
        answer += 1
        
        # 카드 두장 뽑기
        if cur_idx + 2 > n:
            break
        else:
            for i in range(cur_idx, cur_idx + 2):
                new_cards[cards[i]] = True
            cur_idx += 2
        
        # 카드 두 장으로 n+1 만들기
        # origin_cards로 가능한지 확인
        is_possible = False
        for i in range(1000):
            if i in origin_cards:
                if (n + 1) - i in origin_cards:
                    origin_cards.pop(i)
                    origin_cards.pop((n + 1) - i)
                    is_possible = True
                    break
                    
        if not is_possible and coin >= 1:
            for i in range(1000):
                if i in origin_cards:
                    if (n + 1) - i in new_cards:
                        origin_cards.pop(i)
                        new_cards.pop((n + 1) - i)
                        is_possible = True
                        coin -= 1
                        break
                elif i in new_cards:
                    if (n + 1) - i in origin_cards:
                        new_cards.pop(i)
                        origin_cards.pop((n + 1) - i)
                        is_possible = True
                        coin -= 1
                        break           
                        
        if not is_possible and coin >= 2:
            for i in range(1000):
                if i in new_cards:
                    if (n + 1) - i in new_cards:
                        new_cards.pop(i)
                        new_cards.pop((n + 1) - i)
                        is_possible = True
                        coin -= 2
                        break            
        
        if not is_possible:
            break     
        
        
    
    return answer