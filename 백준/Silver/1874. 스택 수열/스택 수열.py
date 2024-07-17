import sys
from collections import deque

input = sys.stdin.readline

data = []
stack = [0]
result = []
i = 1

n = int(input())
for _ in range(n):
    d = int(input())
    data.append(d)
    while i <= d:
        stack.append(i)
        result.append('+')
        i+=1

    if stack[-1] == d:
        stack.pop()
        result.append('-')
    else:
        result = 'NO'
        break

if result == 'NO':
    print(result)
else:
    for r in result:
        print(r)