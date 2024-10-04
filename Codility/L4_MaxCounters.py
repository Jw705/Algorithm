def solution(N, A):
    counters = [0] * N

    max_value = 0 # max counter를 위해 저장하는 변수
    current_base = 0
    for i in range(len(A)):        
        if A[i] == N + 1:
            # max counter
            current_base = max_value
        else:
            # increase(X)
            if counters[A[i] - 1] < current_base:
                counters[A[i] - 1] = current_base + 1
            else:
                counters[A[i] - 1] += 1
            max_value = max(max_value, counters[A[i] - 1])
    
    for i in range(N):
        if counters[i] < current_base:
            counters[i] = current_base

    return counters