import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque()

for _ in range(n):
    data = list(sys.stdin.readline().split())

    if data[0] == 'push':
        queue.append(int(data[1]))
    elif data[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif data[0] == 'size':
        print(len(queue))
    elif data[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif data[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif data[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[len(queue) - 1])
