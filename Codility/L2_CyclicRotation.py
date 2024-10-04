from collections import deque

def solution(A, K):
    q = deque(A)
    for _ in range(K):
        if q:
            q.appendleft(q.pop())
    return list(q)