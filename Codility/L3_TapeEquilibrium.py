def solution(A):
    prefix_sum = [A[0]] + [0] * (len(A)-1)
    prefix_sum_reverse = [0] * (len(A)+1)
    for i in range(len(A)-1,-1,-1):
        prefix_sum_reverse[i] = prefix_sum_reverse[i+1] + A[i]
        
    answer = abs(A[0] - prefix_sum_reverse[1])
    for i in range(1, len(A)-1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]
        answer = min(answer, abs(prefix_sum[i] - prefix_sum_reverse[i+1]))
    return answer