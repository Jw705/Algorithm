import sys
from collections import deque

deque = deque()

n = int(sys.stdin.readline())

for i in range(n):
    deque.append(n - i)

while len(deque) > 1:
    deque.pop()
    deque.appendleft(deque.pop())

print(deque.pop())