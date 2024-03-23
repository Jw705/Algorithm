def solution(s):
    # 각 영단어에 해당하는 숫자를 정의한 사전
    word_to_num = {
        "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
        "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"
    }

    answer = ""
    temp_word = ""  # 영단어를 임시로 저장할 변수

    for char in s:
        if char.isdigit():  # 숫자인 경우
            answer += char
        else:  # 영단어인 경우
            temp_word += char
            
            if temp_word in word_to_num:  # 영단어가 사전에 있는 경우
                answer += word_to_num[temp_word]
                temp_word = ""  # 임시 변수 초기화
                continue

            # 영단어가 아닌 경우, 'zero'부터 'nine'까지의 영단어 중 하나인지 확인
            for word in word_to_num:
                if temp_word.startswith(word):
                    answer += word_to_num[word]
                    temp_word = temp_word[len(word):]  # 영단어 부분을 제거하고 나머지를 저장
                    break

    return int(answer)