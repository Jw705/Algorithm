from collections import deque


def solution(rc, operations):
    n = len(rc)
    m = len(rc[0])
    left_col = deque([rc[i][0] for i in range(n)])
    right_col = deque([rc[i][m - 1] for i in range(n)])
    rows = deque([deque(rc[i][1:m - 1]) for i in range(n)])

    for operation in operations:
        if operation == 'ShiftRow':
            left_col.appendleft(left_col.pop())
            rows.appendleft(rows.pop())
            right_col.appendleft(right_col.pop())
        elif operation == 'Rotate':
            rows[0].appendleft(left_col.popleft())
            right_col.appendleft(rows[0].pop())
            rows[n - 1].append(right_col.pop())
            left_col.append(rows[n - 1].popleft())
            
    answer = []
    for i in range(n):
        answer.append([left_col[i]] + list(rows[i]) + [right_col[i]])
    return answer