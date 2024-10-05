def solution(A):
    N = len(A)

    # prefix_sum[i] = i이후에 존재하는 1의 개수 합
    prefix_sum = [0] * (N - 1) + [A[N - 1]]
    for i in range(N - 2, -1, -1):
        prefix_sum[i] = prefix_sum[i + 1] + A[i]

    answer = 0
    for i in range(N):
        if A[i] == 0:
            answer += prefix_sum[i]
        if answer > 1000000000:
            return -1

    return answer