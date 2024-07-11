import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    q = deque()
    for i in range(n):
        q.append([data[i], i])

    cnt = 1
    while (q):
        if q[0][0] == max(q, key=lambda x: x[0])[0]:
            if q[0][1] == m:
                print(cnt)
                break
            cnt += 1
            q.popleft()
        else:
            tmp = q.popleft()
            q.append([tmp[0], tmp[1]])
