def solution(N):
    answer = 0
    gap_length = 0
    for num in bin(N)[2:]:
        if num == '0':
            gap_length += 1
        else:
            answer = max(answer,gap_length)
            gap_length = 0
    return answer