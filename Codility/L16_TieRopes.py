def solution(K, A):
    answer = 0
    temp_tie_rope_length = 0
    for rope_length in A:
        if rope_length >= K:
            answer += 1
            temp_tie_rope_length = 0
        else:
            temp_tie_rope_length += rope_length
            if temp_tie_rope_length >= K:
                answer += 1
                temp_tie_rope_length = 0

    return answer