def solution(A):
    N = len(A)
    count_list = [1] + [0] * (N + 1)
    for num in A:
        count_list[num] = 1
    return count_list.index(0)